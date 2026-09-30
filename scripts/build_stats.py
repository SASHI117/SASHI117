"""Build the profile stats card from the GitHub API.

    GITHUB_TOKEN=... python scripts/build_stats.py --user SASHI117 --out dist

Written instead of using a public stats service: the popular hosted
instances are frequently rate-limited or down, which leaves broken images
on a profile. This runs in the profile repo's own workflow.
"""
import argparse
import http.client
import json
import os
import time
import urllib.request
from pathlib import Path

LANG_COLORS = {  # github/linguist colours
    "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "HTML": "#e34c26",
    "CSS": "#663399", "Jupyter Notebook": "#DA5B0B", "Dockerfile": "#384d54", "Shell": "#89e051",
    "C++": "#f34b7d", "C": "#555555", "Java": "#b07219", "TSQL": "#e38c00", "PowerShell": "#012456",
}
THEMES = {
    "dark": dict(bg="#0a0a0a", card="#111111", edge="#262626", ink="#fafafa", muted="#8a8a93", a1="#22d3ee", a2="#a78bfa"),
    "light": dict(bg="#ffffff", card="#f6f8fa", edge="#d0d7de", ink="#1f2328", muted="#656d76", a1="#0891b2", a2="#7c3aed"),
}
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"


def api(path: str, attempts: int = 4):
    """GET with retries: the API occasionally answers 5xx or a non-JSON body."""
    req = urllib.request.Request(f"https://api.github.com{path}", headers={
        "Accept": "application/vnd.github+json",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.getenv("GITHUB_TOKEN") else {}),
    })
    for i in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except (OSError, http.client.HTTPException, ValueError):   # URLError, resets, bad JSON
            if i == attempts - 1:
                raise
            time.sleep(2 ** i)


def latest_default_branch_run(user: str, repo: dict):
    """Latest *finished* workflow run on the default branch.

    Filtered client-side: the API's ?branch= filter was observed to return
    empty lists. Unfinished runs are skipped, otherwise this very workflow
    counts itself as a non-passing run while it is still executing.
    """
    runs = api(f"/repos/{user}/{repo['name']}/actions/runs?per_page=30").get("workflow_runs", [])
    return next((r for r in runs
                 if r["head_branch"] == repo["default_branch"] and r["status"] == "completed"), None)


def collect(user: str) -> dict:
    repos = [r for r in api(f"/users/{user}/repos?per_page=100&type=owner") if not r["fork"]]
    langs: dict[str, int] = {}
    ci_green = ci_total = 0
    for r in repos:
        if r.get("disabled"):
            continue
        for lang, n in api(f"/repos/{user}/{r['name']}/languages").items():
            langs[lang] = langs.get(lang, 0) + n
        if r.get("disabled") or r.get("archived"):
            continue
        run = latest_default_branch_run(user, r)
        if run:
            ci_total += 1
            ci_green += run.get("conclusion") == "success"
    return {
        "repos": len(repos),
        "stars": sum(r["stargazers_count"] for r in repos),
        "ci_green": ci_green,
        "ci_total": ci_total,
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


def card(s: dict, t: dict) -> str:
    w, h = 1200, 222
    total = sum(n for _, n in s["langs"]) or 1
    top = s["langs"][:6]
    other = total - sum(n for _, n in top)
    segs = top + ([("Other", other)] if other > 0 else [])

    # stacked language bar
    x, bar = 40.0, []
    for lang, n in segs:
        seg_w = (w - 80) * n / total
        bar.append(f'<rect x="{x:.1f}" y="142" width="{max(seg_w - 2, 0):.1f}" height="14" rx="4" '
                   f'fill="{LANG_COLORS.get(lang, "#6e7681")}"/>')
        x += seg_w
    legend, lx = [], 40
    for lang, n in segs:
        label = f"{lang} {100 * n / total:.1f}%"
        legend.append(f'<circle cx="{lx + 7}" cy="184" r="7" fill="{LANG_COLORS.get(lang, "#6e7681")}"/>'
                      f'<text x="{lx + 20}" y="191" style="font:500 19px {SANS}" fill="{t["muted"]}">{label}</text>')
        lx += 34 + 10.2 * len(label)

    main_lang, main_n = s["langs"][0] if s["langs"] else ("-", 0)
    stats = [("public repositories", s["repos"]),
             ("repos with passing CI", f'{s["ci_green"]}/{s["ci_total"]}'),
             (f"of the code is {main_lang}", f"{100 * main_n / total:.0f}%")]
    tiles = []
    for i, (label, value) in enumerate(stats):
        tx = 40 + i * 330
        tiles.append(f'<text x="{tx}" y="88" style="font:700 44px {SANS}" fill="{t["ink"]}">{value}</text>'
                     f'<text x="{tx}" y="118" style="font:500 19px {SANS}" fill="{t["muted"]}">{label}</text>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"
  aria-label="{s['repos']} public repositories, {s['ci_green']} of {s['ci_total']} repositories with passing CI. Languages: {', '.join(f'{lang} {100 * n / total:.0f}%' for lang, n in segs)}.">
<defs><linearGradient id="acc" x1="0" x2="1"><stop offset="0" stop-color="{t['a1']}"/><stop offset="1" stop-color="{t['a2']}"/></linearGradient></defs>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="16" fill="{t['card']}" stroke="{t['edge']}"/>
<rect x="40" y="28" width="56" height="4" rx="2" fill="url(#acc)"/>
<text x="{w - 40}" y="40" text-anchor="end" style="font:500 16px {SANS}" fill="{t['muted']}">own repositories · refreshed daily</text>
{''.join(tiles)}
{''.join(bar)}
{''.join(legend)}
</svg>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="SASHI117")
    ap.add_argument("--out", type=Path, default=Path("dist"))
    args = ap.parse_args()
    s = collect(args.user)
    args.out.mkdir(parents=True, exist_ok=True)
    for name, t in THEMES.items():
        (args.out / f"stats-{name}.svg").write_text(card(s, t), encoding="utf-8")
    print(json.dumps({k: v for k, v in s.items() if k != "langs"} | {"top_langs": s["langs"][:6]}))


if __name__ == "__main__":
    main()

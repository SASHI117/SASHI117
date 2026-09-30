"""Generate the animated SVGs used in the profile README.

    python scripts/make_art.py        # writes assets/*-{dark,light}.svg

Everything is plain SVG + CSS/SMIL animation: GitHub serves README images
through its image proxy, which allows animation but not scripts or web fonts,
so only system font stacks are used.
"""
import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"

THEMES = {
    "dark": dict(
        bg0="#0b1020", bg1="#1a1142", ink="#f8fafc", sub="#cbd5e1", muted="#94a3b8",
        a1="#22d3ee", a2="#a78bfa", a3="#fbbf24", card="#111827", edge="#334155",
        dot="#ffffff", dot_op=".05", pill="#1e293b",
    ),
    "light": dict(
        bg0="#f8fafc", bg1="#ede9fe", ink="#0f172a", sub="#334155", muted="#64748b",
        a1="#0891b2", a2="#7c3aed", a3="#d97706", card="#ffffff", edge="#cbd5e1",
        dot="#0f172a", dot_op=".05", pill="#f1f5f9",
    ),
}

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Inter, Helvetica, Arial, sans-serif"
MONO = "'Cascadia Code', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
INDIC = "'Nirmala UI', 'Noto Sans Devanagari', 'Noto Sans Telugu', 'Kohinoor Devanagari', sans-serif"


def defs(t, w, h):
    return f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{t['bg0']}"/><stop offset="1" stop-color="{t['bg1']}"/>
  </linearGradient>
  <linearGradient id="acc" x1="0" x2="1">
    <stop offset="0" stop-color="{t['a1']}"/><stop offset="1" stop-color="{t['a2']}"/>
  </linearGradient>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="{t['dot']}" opacity="{t['dot_op']}"/>
  </pattern>
  <clipPath id="frame"><rect width="{w}" height="{h}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#dots)"/>
</g>"""


# --------------------------------------------------------------- header ---
def header(t):
    w, h = 1200, 330
    rng = random.Random(7)
    bars = []
    x0, n, bw, gap = 60, 64, 6, 4
    for i in range(n):
        # a speech-like envelope: two "words" with a pause between them
        env = max(math.sin(math.pi * i / 30) if i < 30 else 0, math.sin(math.pi * (i - 34) / 30) if i >= 34 else 0)
        hgt = 10 + 70 * env * (0.55 + 0.45 * rng.random())
        delay = -rng.random() * 1.4
        dur = 0.9 + rng.random() * 0.9
        x = x0 + i * (bw + gap)
        bars.append(
            f'<rect class="bar" x="{x}" y="{255 - hgt / 2:.1f}" width="{bw}" height="{hgt:.1f}" rx="3" '
            f'fill="url(#acc)" style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s"/>'
        )
    # The waveform "decodes" into words. Each row is one meaning written in
    # Hindi, Telugu and English: farmer, then crop.
    rows = [[("किसान", INDIC), ("రైతు", INDIC), ("farmer", SANS)],
            [("फ़सल", INDIC), ("పంట", INDIC), ("crop", SANS)]]
    pills, pw, k = [], 118, 0
    for r, row in enumerate(rows):
        for c, (word, font) in enumerate(row):
            px, py = 752 + c * (pw + 12), 226 + r * 42
            pills.append(
                f'<g class="tok" style="animation-delay:{k * 0.4:.2f}s">'
                f'<rect x="{px}" y="{py}" width="{pw}" height="32" rx="16" fill="{t["pill"]}" stroke="url(#acc)"/>'
                f'<text x="{px + pw / 2}" y="{py + 22}" text-anchor="middle" '
                f'style="font:600 16px {font}" fill="{t["ink"]}">{word}</text></g>'
            )
            k += 1
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"
  aria-label="Sashi Vardhan Pragada, AI/ML engineer. An animated speech waveform turns into words in Hindi, Telugu and English.">
<style>
  .bar {{ transform-box: fill-box; transform-origin: center; animation: talk 1.4s ease-in-out infinite alternate; }}
  @keyframes talk {{ from {{ transform: scaleY(.22); }} to {{ transform: scaleY(1); }} }}
  .tok {{ opacity: 0; animation: tok 7s ease-in-out infinite; }}
  @keyframes tok {{ 0%, 12% {{ opacity: 0; transform: translateX(-14px); }} 22%, 80% {{ opacity: 1; transform: translateX(0); }} 92%, 100% {{ opacity: 0; }} }}
  .arrow {{ stroke-dasharray: 6 8; animation: flow 1.2s linear infinite; }}
  @keyframes flow {{ to {{ stroke-dashoffset: -28; }} }}
  .cursor {{ animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{ .bar, .tok, .arrow, .cursor {{ animation: none; opacity: 1; }} }}
</style>
{defs(t, w, h)}
<text x="60" y="92" style="font:700 54px {SANS}" fill="{t['ink']}">Sashi Vardhan Pragada</text>
<text x="62" y="134" style="font:500 22px {SANS}" fill="{t['sub']}">AI/ML engineer · speech systems · LLMs &amp; RAG · real-time inference on CPUs</text>
<text x="62" y="168" style="font:500 15px {MONO}" fill="{t['muted']}">Hyderabad, India  ·  AUDICLABS  ·  previously FarmVaidya.ai<tspan class="cursor" fill="{t['a1']}"> ▍</tspan></text>
<text x="60" y="206" style="font:600 12px {MONO}; letter-spacing:2px" fill="{t['muted']}">AUDIO IN</text>
<text x="752" y="206" style="font:600 12px {MONO}; letter-spacing:2px" fill="{t['muted']}">TEXT OUT</text>
{''.join(bars)}
<path class="arrow" d="M 708 255 L 730 255" stroke="{t['a3']}" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M 726 249 L 734 255 L 726 261" stroke="{t['a3']}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
{''.join(pills)}
</svg>
"""


# ------------------------------------------------------------- pipeline ---
STAGES = [
    ("Noisy speech", "field audio", "many languages"),
    ("Separation", "ConvTasNet", "voice vs. noise"),
    ("Speech-to-text", "IndicConformer", "22 Indian langs"),
    ("Hybrid RAG", "semantic + keyword", "+ reranking"),
    ("LLM", "Gemini Live", "Gemma-3 + LoRA"),
    ("Text-to-speech", "spoken reply", "back to the user"),
]


def pipeline(t):
    w, h = 1200, 232
    n, bw, bh, y = len(STAGES), 162, 100, 66
    gap = (w - 2 * 40 - n * bw) / (n - 1)
    xs = [40 + i * (bw + gap) for i in range(n)]
    cycle = 6.0
    boxes, links = [], []
    for i, (title, sub1, sub2) in enumerate(STAGES):
        x = xs[i]
        begin = i * cycle / n
        boxes.append(f"""<g>
  <rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="14" fill="{t['card']}" stroke="{t['edge']}" stroke-width="1.5"/>
  <rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="14" fill="none" stroke="url(#acc)" stroke-width="2.5" opacity="0">
    <animate attributeName="opacity" values="0;1;0" keyTimes="0;.12;.35" dur="{cycle}s" begin="{begin:.2f}s" repeatCount="indefinite"/>
  </rect>
  <text x="{x + bw / 2}" y="{y + 38}" text-anchor="middle" style="font:700 16px {SANS}" fill="{t['ink']}">{title}</text>
  <text x="{x + bw / 2}" y="{y + 63}" text-anchor="middle" style="font:500 12px {MONO}" fill="{t['muted']}">{sub1}</text>
  <text x="{x + bw / 2}" y="{y + 81}" text-anchor="middle" style="font:500 12px {MONO}" fill="{t['muted']}">{sub2}</text>
</g>""")
        if i < n - 1:
            x1, x2 = x + bw, xs[i + 1]
            links.append(
                f'<path class="link" d="M {x1 + 4} {y + bh / 2} L {x2 - 6} {y + bh / 2}" stroke="{t["a2"]}" '
                f'stroke-width="2" fill="none" stroke-linecap="round"/>'
                f'<path d="M {x2 - 11} {y + bh / 2 - 5} L {x2 - 5} {y + bh / 2} L {x2 - 11} {y + bh / 2 + 5}" '
                f'stroke="{t["a2"]}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            )
    track = f"M {xs[0] + bw / 2} {y + bh + 26} L {xs[-1] + bw / 2} {y + bh + 26}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"
  aria-label="Animated voice pipeline: noisy speech, speech separation, speech-to-text, hybrid RAG, LLM, text-to-speech.">
<style>
  .link {{ stroke-dasharray: 5 7; animation: flow 1s linear infinite; }}
  @keyframes flow {{ to {{ stroke-dashoffset: -24; }} }}
  @media (prefers-reduced-motion: reduce) {{ .link {{ animation: none; }} }}
</style>
{defs(t, w, h)}
<text x="40" y="44" style="font:600 13px {MONO}; letter-spacing:2px" fill="{t['muted']}">THE PIPELINE I KEEP BUILDING, ONE STAGE AT A TIME</text>
{''.join(links)}
{''.join(boxes)}
<path d="{track}" stroke="{t['edge']}" stroke-width="2" fill="none" stroke-dasharray="2 6"/>
<circle r="7" fill="{t['a3']}">
  <animateMotion dur="{cycle}s" repeatCount="indefinite" path="{track}"/>
</circle>
<circle r="14" fill="{t['a3']}" opacity=".25">
  <animateMotion dur="{cycle}s" repeatCount="indefinite" path="{track}"/>
  <animate attributeName="r" values="9;16;9" dur="1s" repeatCount="indefinite"/>
</circle>
</svg>
"""


# ------------------------------------------------------------- terminal ---
LINES = [
    ("$ ", "whoami", "cmd"),
    ("", "sashi · AI/ML engineer @ AUDICLABS · Hyderabad", "out"),
    ("$ ", "cat focus.txt", "cmd"),
    ("", "speech for Indian languages · RAG & LLM apps · fast CPU inference", "out"),
    ("$ ", "cat habits.txt", "cmd"),
    ("", "measure before claiming · ship tests with the code · write down what broke", "out"),
]


def terminal(t):
    w, h = 1200, 250
    rows, clips = [], []
    tstart, y = 0.4, 78
    for i, (prompt, text, kind) in enumerate(LINES):
        full = prompt + text
        width = 11.2 * len(full) + 20
        dur = 0.045 * len(text) if kind == "cmd" else 0.35
        color = t["a1"] if kind == "cmd" else t["sub"]
        clips.append(f"""<clipPath id="c{i}"><rect x="40" y="{y - 20}" width="0" height="28">
  <animate attributeName="width" from="0" to="{width:.0f}" begin="{tstart:.2f}s" dur="{dur:.2f}s" fill="freeze"
           calcMode="{'discrete' if kind == 'out' else 'linear'}"/></rect></clipPath>""")
        body = (f'<tspan fill="{t["a3"]}">{prompt}</tspan>{text.replace("&", "&amp;")}' if prompt
                else text.replace("&", "&amp;"))
        rows.append(f'<text x="44" y="{y}" clip-path="url(#c{i})" style="font:500 18px {MONO}" fill="{color}">{body}</text>')
        tstart += dur + (0.25 if kind == "cmd" else 0.6)
        y += 28 if kind == "cmd" else 36
    cursor_y = y - 18
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"
  aria-label="Terminal: whoami, Sashi, AI/ML engineer at AUDICLABS in Hyderabad. Focus: speech for Indian languages, RAG and LLM apps, fast CPU inference. Habits: measure before claiming, ship tests with the code, write down what broke.">
<style>
  .cursor {{ opacity: 0; animation: blink 1s steps(1) {tstart:.2f}s infinite; }}
  @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
</style>
<defs>{''.join(clips)}</defs>
{defs(t, w, h)}
<rect x="0" y="0" width="{w}" height="40" fill="{t['card']}" opacity=".55"/>
<circle cx="26" cy="20" r="6.5" fill="#ff5f57"/><circle cx="48" cy="20" r="6.5" fill="#febc2e"/><circle cx="70" cy="20" r="6.5" fill="#28c840"/>
<text x="{w / 2}" y="25" text-anchor="middle" style="font:500 13px {MONO}" fill="{t['muted']}">sashi@hyderabad: ~</text>
{''.join(rows)}
<rect class="cursor" x="44" y="{cursor_y}" width="11" height="22" fill="{t['a1']}"/>
</svg>
"""


# --------------------------------------------------------------- footer ---
def footer(t):
    w, h = 1200, 90
    pts = " ".join(f"{x},{45 + 16 * math.sin(x / 38) * math.sin(x / 190):.1f}" for x in range(0, w + 1, 6))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Animated waveform divider">
<defs><linearGradient id="acc" x1="0" x2="1"><stop offset="0" stop-color="{t['a1']}"/><stop offset="1" stop-color="{t['a2']}"/></linearGradient></defs>
<style>
  .w {{ stroke-dasharray: 1400; stroke-dashoffset: 1400; animation: draw 5s ease-in-out infinite; }}
  @keyframes draw {{ 45%, 60% {{ stroke-dashoffset: 0; }} 100% {{ stroke-dashoffset: -1400; }} }}
  @media (prefers-reduced-motion: reduce) {{ .w {{ animation: none; stroke-dashoffset: 0; }} }}
</style>
<polyline class="w" points="{pts}" fill="none" stroke="url(#acc)" stroke-width="3" stroke-linecap="round" pathLength="1400"/>
</svg>
"""


def main():
    OUT.mkdir(exist_ok=True)
    for name, fn in [("header", header), ("pipeline", pipeline), ("terminal", terminal), ("divider", footer)]:
        for theme, t in THEMES.items():
            (OUT / f"{name}-{theme}.svg").write_text(fn(t), encoding="utf-8")
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))


if __name__ == "__main__":
    main()

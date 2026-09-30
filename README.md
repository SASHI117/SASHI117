<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Sashi Vardhan Pragada, AI/ML engineer. An animated speech waveform turns into the words farmer and crop in Hindi, Telugu and English." src="assets/header-dark.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/sashi-vardhan-pragada-60634022b"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-sashi--vardhan--pragada-0A66C2?logo=linkedin&logoColor=white"></a>
  <a href="mailto:mesashivardhan4080@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-mesashivardhan4080%40gmail.com-D14836?logo=gmail&logoColor=white"></a>
  <img alt="Location" src="https://img.shields.io/badge/Based%20in-Hyderabad%2C%20India-222?logo=googlemaps&logoColor=white">
</p>

## Hi, I'm Sashi 👋

I build machine-learning systems that have to work outside the notebook:
speech recorded in noisy places, questions that switch between Telugu, Hindi
and English, and models that have to answer on a CPU because there's no GPU
budget. Most of my work sits where speech,
language models and plain software engineering meet. That's where the
hardest bugs live, and the most interesting ones.

I'm an **AI & ML Engineer at AUDICLABS** in Hyderabad, working on real-time
inference on CPUs. Before that I was one of the early engineers at
**FarmVaidya.ai**, building conversational AI for farmers, from speech
datasets and ASR training to fine-tuned open-source LLMs and the benchmarks we
used to decide what to ship.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/terminal-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/terminal-light.svg">
  <img alt="Terminal: whoami prints Sashi, AI/ML engineer at AUDICLABS, Hyderabad. focus.txt: speech for Indian languages, RAG and LLM apps, fast CPU inference. habits.txt: measure before claiming, ship tests with the code, write down what broke." src="assets/terminal-dark.svg" width="100%">
</picture>

## What I work on

**🎙️ Speech, for languages most tools treat as an afterthought.** I benchmark
and self-host speech-to-text for Indian languages, and I've learned that the
evaluation code needs as much care as the models. My benchmark once scored a
*wrong* Hindi transcript as perfect, because of how Python handles Unicode
vowel signs. That story is below.

**🧠 LLMs and retrieval that stay grounded.** Hybrid RAG (semantic + keyword +
reranking) over long domain documents, LoRA fine-tuning of open models on
curated instruction data, and the unglamorous pipeline work of cleaning,
chunking and structuring that makes retrieval good in the first place.

**⚡ Making it fast enough to be real-time on ordinary hardware.** Quantization,
runtime and memory optimization, warm-up and concurrency, and measuring
real-time factor instead of guessing it. A voice assistant that answers in
eight seconds isn't a voice assistant.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pipeline-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/pipeline-light.svg">
  <img alt="Animated pipeline: noisy speech, speech separation with ConvTasNet, speech-to-text with IndicConformer, hybrid RAG, an LLM (Gemini Live or Gemma-3 with LoRA), then text-to-speech." src="assets/pipeline-dark.svg" width="100%">
</picture>

Each box in that diagram maps to something I've built on its own, measured,
and then wired back into the chain:

| Stage | Where it shows up |
|---|---|
| **Separation** | ConvTasNet speech separation in a voice agent, to pull the speaker out of background noise |
| **Speech-to-text** | [ai4bharat_stt](https://github.com/SASHI117/ai4bharat_stt), a self-hosted IndicConformer server for 22 languages. [stt-benchmark-backend](https://github.com/SASHI117/stt-benchmark-backend) compares 8 providers on WER and latency |
| **Retrieval** | Tiered hybrid RAG over a 200+ page knowledge base with sub-second retrieval, and a knowledge-base platform that ingests web pages, documents, images, audio and video |
| **LLM** | Gemma-3-4B fine-tuned with LoRA on agricultural instruction data, streaming Gemini Live for real-time conversation, and a [tool for field experts to author instruction data](https://github.com/SASHI117/llama-dataset-frontend) |
| **Speech out** | STT → LLM → TTS voice pipelines, validated end to end |

## Where I've been

| When | Where | What |
|---|---|---|
| **Jun 2026 – now** | **AUDICLABS** · AI & ML Engineer | Real-time AI inference on CPUs: quantization, runtime and memory optimization, high-concurrency streaming, and portable standalone runtimes for local and edge deployment |
| Dec 2025 – Jun 2026 | **FarmVaidya.ai** · AI & ML Intern | Multilingual conversational AI for agriculture: fine-tuned open LLMs, speech data pipelines, ASR training, data curation and benchmarking with field experts |
| May – Jun 2025 | **Airports Authority of India** · Intern | Telecom software infrastructure, network monitoring, fault-log analysis |
| Sep – Oct 2024 | **BSNL** · Intern | Real-time surveillance, radar and network-monitoring systems; uptime and fault detection |
| 2022 – 2026 | **GITAM University** | B.Tech in Electronics & Communication, Honours in AI & ML |

## Selected projects

<table>
<tr>
<td width="50%" valign="top">

### 🎧 [STT Benchmark](https://github.com/SASHI117/stt-benchmark-backend)
One audio clip goes to **8 speech-to-text providers (11 models)** concurrently,
and each is scored on WER and latency. It was built to compare engines on
Indian-language farmer audio. It has a Unicode-correct scorer for Indic
scripts, bounded polling for async vendor APIs, and a
[web UI](https://github.com/SASHI117/stt-benchmark-frontend).

`FastAPI` `SQLAlchemy` `Docker` `25 tests`

</td>
<td width="50%" valign="top">

### 🗣️ [AI4Bharat STT server](https://github.com/SASHI117/ai4bharat_stt)
Self-hosted speech-to-text for **22 Indian languages** on IndicConformer-600M.
Verified end to end with the real model: Telugu and Hindi transcribed exactly,
**RTF 0.5–0.9 on a laptop CPU**, and a warm-up step that cut the first
request from 11.7 s to 3.0 s. Comes with a
[batch CLI client](https://github.com/SASHI117/users_ai4bharat_stt).

`ONNX Runtime` `FastAPI` `ffmpeg` `Docker`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌿 [Plant Disease Classifier](https://github.com/SASHI117/Plant-Disease-Classification)
MobileNetV2 transfer learning for 15 pepper, potato and tomato conditions.
**94.3%** on validation and **78.7%** on an independent PlantVillage sample.
The gap, and which diseases collapse into which, is analysed in the README.
The model ships in the repo along with a Gradio app, at ~100 ms per image on CPU.

`TensorFlow` `Keras` `Gradio`

</td>
<td width="50%" valign="top">

### 💬 [Debt-Stress FinBERT](https://github.com/SASHI117/Debt-Stress-Prediction-Using-FinBERT)
FinBERT fine-tuned to grade financial stress in banking messages. The first
version reported 100%, which turned out to be train/test sentence overlap.
Evaluated on wording the model has never seen, it scores **54%, 13 points
above a TF-IDF baseline**, and the README explains why.

`Transformers` `PyTorch` `scikit-learn`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌾 [Crop Recommendation + SHAP](https://github.com/SASHI117/Crop_Prediction_Analysis)
Recommends one of 22 crops from soil and weather readings
(**Random Forest, 99.3% CV**). An XGBoost yield model is explained with SHAP,
and because the target formula is known, the explanation itself can be
graded: SHAP gets the ranking right and the magnitudes wrong.

`XGBoost` `SHAP` `scikit-learn`

</td>
<td width="50%" valign="top">

### 📡 [Network Optimizer](https://github.com/SASHI117/Network-Optimizer)
A Streamlit app that combines live cell towers (OpenCelliD) and live weather
with a Random Forest signal-strength model. The model is compared against a
log-distance path-loss baseline and the shadowing noise floor, and can be
retrained on uploaded measurements.

`Streamlit` `scikit-learn` `REST APIs`

</td>
</tr>
</table>

Also: [pro-task-manager](https://github.com/SASHI117/pro-task-manager), a React +
Firebase task manager with per-user Firestore security rules, recurring tasks
and 19 unit tests.

## Things I learned by measuring

The habit I'm proudest of is checking my own headline numbers. Each of these
changed what a project claimed:

<details>
<summary><b>A wrong Hindi transcript scored WER 0.0</b>: Python's <code>\w</code> doesn't match Indic vowel signs</summary>

<br>The benchmark stripped punctuation with `re.sub(r"[^\w\s]", "", text)`.
Devanagari and Telugu vowel signs are Unicode *combining marks*, which `\w`
doesn't match, so they were deleted. **किसान** and the misrecognized
**कसान** both became **कसन**, a perfect match. Every Indic score was
optimistic. The fix strips characters by Unicode category, and a regression
test pins it.
</details>

<details>
<summary><b>…and then a perfect transcript lost 2 words out of 9</b>: nukta and chandrabindu</summary>

<br>Running the real IndicConformer model on a known sentence returned
**गेहूँ / फ़सल** for a reference spelled **गेहूं / फसल**. They're the same
words in two accepted spellings. The scorer now treats those variants as
equal, but not Telugu's arasunna, which is a different sound.
</details>

<details>
<summary><b>100% accuracy that measured memory, not understanding</b></summary>

<br>A FinBERT classifier trained on 2,100 template-generated messages scored
100%. Only 619 of those sentences were distinct, and 74% of the test
sentences also appeared in training. Holding out whole templates dropped it
to 54%, still 13 points above TF-IDF. That's the real number.
</details>

<details>
<summary><b>94.3% in validation, 78.7% on the original dataset</b></summary>

<br>The plant-disease model's validation score came from one Kaggle copy of
PlantVillage. Scoring 150 images from the *original* release with the same
loader gave 78.7%, and showed that two classes absorb others: Septoria takes
70% of bacterial spot. Both numbers are in the README, with the confusion matrix.
</details>

<details>
<summary><b>When a linear regression beats tuned XGBoost</b></summary>

<br>A "yield" model scored R² 0.998, and a plain linear regression scored
0.999, because the target was a formula of the inputs. A benchmark with
a known answer is still useful, though: I used it to check whether SHAP
recovers the true feature contributions. It gets the order right and the
sizes wrong.
</details>

<details>
<summary><b>A model server that couldn't read audio on a new FFmpeg</b></summary>

<br>torchaudio's FFmpeg backend only supports FFmpeg 4–6 and was removed in
torchaudio 2.9, which I discovered by running the server with a current
FFmpeg. Decoding now goes through the ffmpeg CLI directly. The same run
showed the first inference was 4× slower than steady state, so the server
warms up before accepting traffic.
</details>

## Work that isn't on GitHub

These weren't open-sourced, so there's nothing to link, but they're the
closest to what I do day to day:

- **🎙️ Real-time multilingual voice agent** on Gemini Live, with tiered hybrid
  RAG (semantic + keyword + reranking) over a 200+ page knowledge base,
  sub-second retrieval, and ConvTasNet speech separation for noisy
  environments. Speech → RAG → LLM → response, deployed with Docker and FastAPI.
- **📚 Knowledge base and RAG platform** that ingests web pages and documents
  (text, images, audio, video), then cleans, chunks, adds metadata and embeds
  them for vector search, with grounded Q&A exposed over REST APIs.
- **🌱 Agricultural advisory LLM**: Gemma-3-4B fine-tuned with LoRA
  (Unsloth, Hugging Face) on curated instruction data. Merged adapters were
  served with FastAPI on an Azure GPU VM behind Nginx, with HTTPS and API-key
  auth, and validated inside an STT → LLM → TTS voice pipeline.
- **🔊 Real-time speech command recognition**: a compact model on
  time-frequency features, from preprocessing to real-time inference.

## How I like to work

- **Numbers come with their evaluation.** A metric without the split, the
  baseline and the failure cases is a rumour.
- **Tests ship with the code.** Every project above has CI, and most of the
  tests cover the thing that actually broke, not only the happy path.
- **Latency is a feature.** For voice, first-response time matters as much as
  accuracy, so I measure both.
- **Write down what went wrong.** The READMEs describe the bugs I fixed,
  because that's the part other engineers can reuse.

## Toolbox

<p>
  <img alt="Python, C++, C, Java, JavaScript, HTML, CSS" src="https://skillicons.dev/icons?i=py,cpp,c,java,js,html,css&perline=16">
  <br>
  <img alt="PyTorch, TensorFlow, scikit-learn, OpenCV, FastAPI, Flask, React, Tailwind" src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,opencv,fastapi,flask,react,tailwind&perline=16">
  <br>
  <img alt="Docker, Azure, GCP, AWS, Firebase, Vercel, Linux, Git, GitHub, GitHub Actions, Postgres, SQLite" src="https://skillicons.dev/icons?i=docker,azure,gcp,aws,firebase,vercel,linux,git,github,githubactions,postgres,sqlite&perline=16">
</p>

<details>
<summary><b>The full list</b></summary>
<br>

- **Languages:** Python, C++, C, Java, JavaScript, HTML, CSS
- **ML / DL / NLP:** classical ML models, PyTorch, Transformers, SFT, PEFT / LoRA, FinBERT, neural networks, regression analysis, Random Forest, XGBoost, model optimization and quantization, Generative AI, multimodal AI, document intelligence, information extraction
- **Generative AI & RAG:** LLMs and SLMs, LangChain, LangGraph, RAG pipelines, knowledge-base construction, embeddings, vector, hybrid and keyword search, reranking, RAG tuning and retrieval optimization, prompt engineering, AI agents and agentic AI
- **Speech & multimodal:** STT → LLM → TTS pipelines, real-time voice AI, speech technology and separation, ASR evaluation (WER), audio, image, video and text processing, multimodal data processing
- **Serving & apps:** FastAPI, REST APIs, real-time AI systems, AI web apps and automation, Streamlit, Gradio, React, dashboards, web crawling and scraping, content extraction, document parsing
- **Tools & infra:** Git, GitHub, Hugging Face, Unsloth, Pipecat, Sherpa-ONNX, ONNX Runtime, Docker, CI/CD (GitHub Actions), Azure, GCP, AWS, Vercel, Render, Railway, Firebase, Microsoft Excel
- **Practice:** dataset building and curation, data pipelines, model evaluation and benchmarking, error analysis, latency optimization, data structures and algorithms, problem solving

</details>

## On GitHub

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/SASHI117/SASHI117/output/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/SASHI117/SASHI117/output/stats-light.svg">
  <img alt="Profile statistics: public repositories, repositories with passing CI, and language breakdown." src="https://raw.githubusercontent.com/SASHI117/SASHI117/output/stats-dark.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/SASHI117/SASHI117/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/SASHI117/SASHI117/output/snake-light.svg">
  <img alt="A snake animation eating the contribution graph" src="https://raw.githubusercontent.com/SASHI117/SASHI117/output/snake-light.svg" width="100%">
</picture>

<sub>The header, terminal, pipeline and divider are hand-made SVGs generated by
[`scripts/make_art.py`](scripts/make_art.py). The stats card is built daily by
[`scripts/build_stats.py`](scripts/build_stats.py) in this repo's own workflow,
not by a hosted service.</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/divider-light.svg">
  <img alt="" src="assets/divider-dark.svg" width="100%">
</picture>

<p align="center">
  If any of this overlaps with what you're building, speech for Indian
  languages, grounded LLM apps or squeezing models onto modest hardware,
  I'd like to hear about it. <b>mesashivardhan4080@gmail.com</b>
</p>

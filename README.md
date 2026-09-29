### Sashi Vardhan Pragada

AI/ML engineer in Hyderabad. I build speech and language systems that have to
survive real conditions: noisy audio, Indian languages, CPU-only budgets,
and users on unreliable connections.

- **Now:** AI & ML Engineer at **AUDICLABS**. I work on real-time inference on
  CPUs: quantization, runtime and memory optimization, high-concurrency
  streaming, and standalone runtimes for local and edge deployment.
- **Before:** AI/ML intern at **FarmVaidya.ai**, where I built multilingual
  conversational AI for farmers: fine-tuned open-source LLMs, speech datasets
  and ASR training, and the benchmarks we used to choose between models.
- **Education:** B.Tech in ECE with Honours in AI & ML, GITAM University (2022–2026).

A habit you'll see in these repos: I measure before I claim. Several of them
include the evaluation that *lowered* the headline number, because knowing
that is the useful part.

---

#### Speech & LLM systems

| Repo | What it does | Worth a look |
|---|---|---|
| [stt-benchmark-backend](https://github.com/SASHI117/stt-benchmark-backend) · [frontend](https://github.com/SASHI117/stt-benchmark-frontend) | Sends one clip to 8 STT providers (11 models) concurrently and scores WER and latency | Found that the WER normalizer deleted Indic vowel signs, so a *wrong* Hindi transcript scored WER 0.0 |
| [ai4bharat_stt](https://github.com/SASHI117/ai4bharat_stt) · [client](https://github.com/SASHI117/users_ai4bharat_stt) | Self-hosted speech-to-text for 22 Indian languages on AI4Bharat IndicConformer-600M, with FastAPI and Docker | Lazy model loading, thread-pooled inference, real-time factor reported per request |
| [llama-dataset-frontend](https://github.com/SASHI117/llama-dataset-frontend) | Tool for agronomists to write multi-turn Q/A instruction data for LLM fine-tuning | Data tagged by crop and reasoning type, in `user`/`model` chat format |
| [Debt-Stress-Prediction-Using-FinBERT](https://github.com/SASHI117/Debt-Stress-Prediction-Using-FinBERT) | FinBERT fine-tuned to grade financial stress in banking messages | Reported 100% turned out to be train/test sentence overlap. On held-out wording it's 54%, +13 points over TF-IDF |

#### Applied ML

| Repo | What it does | Worth a look |
|---|---|---|
| [Plant-Disease-Classification](https://github.com/SASHI117/Plant-Disease-Classification) | MobileNetV2 transfer learning for 15 leaf diseases, with a Gradio app and the model included | 94.3% on validation, 78.7% on an independent PlantVillage sample, with per-class error analysis |
| [Crop_Prediction_Analysis](https://github.com/SASHI117/Crop_Prediction_Analysis) | Crop recommendation (22 crops, RF 99.3% CV) plus XGBoost with SHAP | SHAP checked against a *known* ground-truth formula: it gets the ranking right and the magnitudes wrong |
| [Network-Optimizer](https://github.com/SASHI117/Network-Optimizer) | Streamlit app combining live OpenCelliD towers and OpenWeather data with a Random Forest RSSI model | Evaluated against a log-distance path-loss baseline and the shadowing noise floor |
| [pro-task-manager](https://github.com/SASHI117/pro-task-manager) | React + Firebase task manager with per-user Firestore rules | Timezone and recurrence bugs fixed, with unit tests |

#### Work that isn't public

These aren't open-sourced, so there's nothing to link. This is what they covered:

- **Real-time multilingual voice agent** on Gemini Live, with tiered hybrid RAG
  (semantic + keyword + reranking) over a 200+ page knowledge base,
  sub-second retrieval, and ConvTasNet speech separation for noisy
  environments. Speech → RAG → LLM → response, deployed with Docker and FastAPI.
- **Knowledge base and RAG platform** that ingests web pages and documents
  (text, images, audio, video), then cleans, chunks, adds metadata and
  embeds them for vector search, with grounded Q&A over REST APIs.
- **Agricultural advisory LLM:** Gemma-3-4B fine-tuned with LoRA (Unsloth,
  Hugging Face) on curated instruction data. Merged adapters were served with
  FastAPI on an Azure GPU VM behind Nginx, with HTTPS and API-key auth, and
  validated inside an STT → LLM → TTS voice pipeline.
- **Real-time speech command recognition:** a compact model on
  time-frequency features, built end to end from preprocessing to real-time inference.

<details>
<summary><b>Skills</b></summary>

- **Languages:** Python, C++, C, Java, JavaScript, HTML, CSS
- **ML / DL / NLP:** PyTorch, Transformers, SFT, PEFT / LoRA, FinBERT, neural networks, regression analysis, Random Forest, XGBoost, model optimization and quantization, Generative AI, multimodal AI, document intelligence, information extraction
- **Generative AI & RAG:** LLMs and SLMs, LangChain, LangGraph, RAG pipelines, knowledge-base construction, embeddings, vector, hybrid and keyword search, reranking, RAG tuning and retrieval optimization, prompt engineering, AI agents and agentic AI
- **Speech & multimodal:** STT → LLM → TTS pipelines, real-time voice AI, speech technology and separation, ASR evaluation (WER), audio, image, video and text processing, multimodal data processing
- **Serving & apps:** FastAPI, REST APIs, real-time AI systems, AI web apps and automation, Streamlit, Gradio, React, dashboards, web crawling and scraping, content extraction, document parsing
- **Tools & infra:** Git, Hugging Face, Unsloth, Pipecat, Sherpa-ONNX, ONNX Runtime, Docker, CI/CD (GitHub Actions), Azure, GCP, AWS, Vercel, Render, Railway, Firebase, Microsoft Excel
- **Practice:** dataset building and curation, data pipelines, model evaluation and benchmarking, error analysis, latency optimization, data structures and algorithms, problem solving

</details>

Earlier internships: Airports Authority of India and BSNL, on network
monitoring and reliability in real-time communication systems.

📫 mesashivardhan4080@gmail.com

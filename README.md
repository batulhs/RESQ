<div align="center">

# 🛡️ RESQ

### *Women's Safety & Support Chatbot*

A calm, supportive AI companion for safety guidance, emotional support, and quick access to help - powered by a locally-run large language model.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Transformers](https://img.shields.io/badge/🤗_Transformers-FFD21E)
![Model](https://img.shields.io/badge/Zephyr--7B--Beta-4--bit-8B5FBF)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

</div>

---

## ✨ Overview

**RESQ** provides conversational support, emotional assistance, and safety guidance through a clean web interface. The backend runs the [**Zephyr-7B-Beta**](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) large language model **locally in 4-bit quantization** on a GPU (via Google Colab), served through a **FastAPI** endpoint and exposed with **ngrok**.

---

## 🌸 Features

-  **AI chatbot** powered by Zephyr-7B-Beta, run locally with 4-bit (NF4) quantization
-  **Multi-turn memory** with a sliding conversation window
-  **Emergency panic button** - plays an audible alarm (Web Audio API) + on-screen safety guidance (call 112)
-  **Quick-action prompts** for legal help, mental health, safe places, and helplines
-  **Markdown-rendered replies** for clean, readable, formatted responses
-  Calm, responsive chat interface

---

## 🧩 Tech Stack

| Layer        | Technology                                      |
| ------------ | ----------------------------------------------- |
|  Frontend  | HTML, CSS, JavaScript (Markdown via `marked`)   |
|  Backend   | Python, FastAPI, Uvicorn                        |
|  AI Model  | `HuggingFaceH4/zephyr-7b-beta`                  |
|  Inference | Transformers + bitsandbytes (4-bit, local GPU)  |
|  Tunneling | ngrok                                           |

---

## 🏗️ How It Works

The model is too large for a typical laptop, so the backend runs in **Google Colab** on a GPU:
1. Colab loads Zephyr-7B-Beta in 4-bit quantization and serves it via a FastAPI `/chat` endpoint.
2. ngrok exposes that endpoint at a stable public URL.
3. The frontend sends messages to that URL and renders the replies.

---

## 🚀 Setup

### 1️⃣ Backend (Google Colab)

Open the backend code in a Colab notebook with a **GPU runtime**
*(Runtime → Change runtime type → T4 GPU)*, then install dependencies:

```bash
pip install -q -U transformers accelerate bitsandbytes pyngrok hf_transfer fastapi uvicorn nest_asyncio
```

> ⚠️ **Restart the runtime after installing** - this is required for `bitsandbytes` to load correctly.

Then:

-  Add your **ngrok auth token** to Colab **Secrets** as `NGROK_AUTH` *(get one at [ngrok.com](https://ngrok.com))*
-  *(Optional)* set a **static ngrok domain** in `NGROK_DOMAIN` so the public URL never changes
-  Run the backend cell - it prints a public URL

### 2️⃣ Frontend

- In `templates/index.html`, set `API_URL` to your ngrok URL (with `/chat` at the end)
- Open the HTML file in a browser and start chatting 💜

> 💡 The Colab cell must stay running while you use the chatbot.

---

## 🔌 API

| Method | Route   | Description                                                     |
| ------ | ------- | -------------------------------------------------------------- |
| `GET`  | `/`     | Health check                                                   |
| `POST` | `/chat` | Accepts `{ "message": "..." }`, returns `{ "response": "..." }` |

---

## 🔐 Security Notes

-  The ngrok token is read from Colab **Secrets**, never hardcoded
-  Databases, session files, and user data are **never** committed *(see `.gitignore`)*
-  **Never commit secrets or API keys to version control**

---

## 🌱 Limitations & Future Work

- Runs in Colab - the session must stay alive *(not a persistent deployment)*
- Conversation history is shared globally, not per-user
- **Planned:** persistent hosting · per-session conversations · SMS/location alerts · multilingual support

---

<div align="center">


📚 *For academic and learning purposes only*

</div>

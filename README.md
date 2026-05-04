# RESQ 🤝

**Women's Safety & Support Chatbot**

RESQ is a Flask-based AI chatbot that provides real-time conversational support, emotional assistance, and safety-related guidance through a simple web interface. It is powered by the [Hugging Face Zephyr-7B-Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) model via the Hugging Face Inference API.

---

## 📌 Features

- 🤖 AI-powered chatbot (Zephyr-7B-Beta via Hugging Face Inference API)
- 🚨 Panic button for emergency alerts
- 📍 Geolocation-based safe place suggestions
- 📞 Quick access to helpline numbers
- 🎧 Alarm/sound feature for emergencies
- 💬 Mental health and emotional support responses
- 🔐 Secure login system
- 🎨 Calm and user-friendly interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| AI Model | HuggingFaceH4/zephyr-7b-beta |
| AI Inference | Hugging Face Inference API |
| Data | JSON, SQLite (`resq.db`) |

---

## 📂 Project Structure

```
RESQ/
├── static/          # CSS, JS, images
├── templates/       # HTML templates
├── flask_session/   # Server-side session storage
├── app.py           # Main Flask application
├── resq.db          # SQLite database
├── users.json       # User data (local)
├── .gitignore       # Ignored files
└── README.md        # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/batulhs/RESQ.git
cd RESQ
```

### 2. Create and activate a virtual environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Hugging Face API token

Create a `.env` file in the project root:

```
HF_TOKEN=your_huggingface_token_here
```

> Get your token at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).  
> The model used is `HuggingFaceH4/zephyr-7b-beta`.

### 5. Run the application

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000`.

---

## 🔌 API Endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/` | Renders the main chat interface |
| POST | `/chat` | Accepts `{ "message": "..." }` JSON, returns `{ "response": "..." }` |

---

## 🔐 Security Notes

- API tokens are loaded from environment variables via `os.getenv("HF_TOKEN")`.
- Sensitive files (`.env`, session data) are excluded via `.gitignore`.
- **Never commit secrets or API keys to version control.**

---

## 🎯 Future Improvements

- [ ] Mobile app version
- [ ] SMS-based emergency alerts
- [ ] Live location sharing with trusted contacts
- [ ] Multilingual support
- [ ] Advanced AI safety classification

---

## 📜 License

This project is for academic and learning purposes only.

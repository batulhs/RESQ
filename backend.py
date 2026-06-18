import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"   # fast parallel downloader (set BEFORE importing HF libs)

import re, torch, asyncio, nest_asyncio
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from pyngrok import ngrok
import uvicorn
from google.colab import userdata

# CONFIG
MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
NGROK_DOMAIN = "impedible-nonvituperatively-karon.ngrok-free.dev"  # domain only, no https:// or /chat
MAX_TURNS = 6


nest_asyncio.apply()

# Load model (downloads to local Colab disk)
print("📥 Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("📥 Loading model with 4-bit quantization...")
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
    use_safetensors=True,   # skip duplicate .bin weights, download only safetensors
)
print("✅ Model loaded successfully!")

# FastAPI 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_history = []

SYSTEM_PROMPT = (
    "You are RESQ, a calm, supportive assistant for women's safety, mental health, "
    "and legal aid. Give clear, empathetic, kind responses of 3-6 short sentences. "
    "Speak warmly and directly, like a trusted friend. Avoid repeating yourself or rambling. "
    "Use Markdown: **bold** for key terms, and bullet points (- ) only for lists of "
    "resources or step-by-step actions. Always end with a complete thought."
)

def clean_response(text: str) -> str:
    """Tidy raw model output into clean Markdown."""
    text = text.strip()
    text = re.sub(r"^(<\|\w+\|>)+", "", text).strip()
    text = re.sub(r"^(User:|Assistant:|RESQ:)\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if text and text[-1] not in ".!?":
        last = max(text.rfind("."), text.rfind("!"), text.rfind("?"))
        if last != -1:
            text = text[:last + 1]
    return text.strip()

@app.get("/")
def home():
    return {"message": "RESQ backend is running 🚀"}

@app.post("/chat")
async def chat(request: Request):
    global chat_history
    data = await request.json()
    user_input = data.get("message", "").strip()
    if not user_input:
        return {"response": "I didn't receive any message."}

    chat_history.append({"role": "user", "content": user_input})

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_history[-MAX_TURNS * 2:]

    inputs = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        add_generation_prompt=True,
        return_dict=True,
    ).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id,
    )

    full = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = full.split("<|assistant|>")[-1].strip() if "<|assistant|>" in full else full.strip()
    response = clean_response(response)

    chat_history.append({"role": "assistant", "content": response})
    if len(chat_history) > MAX_TURNS * 2:
        chat_history = chat_history[-MAX_TURNS * 2:]

    return {"response": response}

# Expose with ngrok
token = userdata.get("NGROK_AUTH")
if token:
    ngrok.set_auth_token(token)

if NGROK_DOMAIN:
    public_url = ngrok.connect(8000, domain=NGROK_DOMAIN)
else:
    public_url = ngrok.connect(8000)
print("🌐 Public URL:", public_url)

config = uvicorn.Config(app, host="0.0.0.0", port=8000)
server = uvicorn.Server(config)
try:
    asyncio.run(server.serve())
except KeyboardInterrupt:
    print("Server stopped.")
finally:
    try:
        ngrok.disconnect(public_url)
    except Exception:
        pass

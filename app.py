# app.py
import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

HF_TOKEN = os.getenv("HF_TOKEN")  # store your token as env var
MODEL = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_huggingface(prompt):
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 150}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        return f"⚠️ Error from Hugging Face API: {response.text}"
    data = response.json()
    # Hugging Face returns list of dicts
    if isinstance(data, list) and "generated_text" in data[0]:
        return data[0]["generated_text"]
    return str(data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "No input provided"}), 400
    bot_response = query_huggingface(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

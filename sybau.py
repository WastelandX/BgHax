import requests
import os
import time

API_KEY = os.getenv("HF_TOKEN")
if not API_KEY:
    print("❌ HF_TOKEN not set")
    exit()

MODEL = "google/gemma-2b-it"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

history = []

def ask_ai(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0.8,
            "top_p": 0.9,
            "repetition_penalty": 1.3,
            "return_full_text": False
        }
    }

    r = requests.post(API_URL, headers=headers, json=payload)
    if r.status_code != 200:
        return "⚠️ Model loading or rate-limited. Try again."

    data = r.json()
    return data[0]["generated_text"].strip()

print("=" * 40)
print(" Sybau-GPT • HuggingFace AI")
print(" Type 'exit' to quit")
print("=" * 40)

while True:
    user = input("You > ").strip()
    if user.lower() == "exit":
        break

    history.append(f"User: {user}")
    context = "\n".join(history[-4:]) + "\nAI:"

    print("Sybau-GPT > thinking...")
    reply = ask_ai(context)

    print("Sybau-GPT >", reply)
    history.append(f"AI: {reply}")
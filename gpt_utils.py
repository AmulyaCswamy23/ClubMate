import requests

def ask_gpt(prompt: str, model="mistral"):
response = requests.post(
"http://localhost:11434/api/generate",
json={"model": model, "prompt": prompt, "stream": False}
)
data = response.json()
return data['response']
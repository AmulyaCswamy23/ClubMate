# main.py
from fastapi import FastAPI
from gpt_utils import ask_gpt
from calendar_utils import create_event, list_events
from telegram_utils import send_telegram_message

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Club Assistant is running."}

@app.post("/email")
def generate_email(prompt: str):
    return {"email": ask_gpt(f"Write a professional email: {prompt}")}

@app.post("/agenda")
def generate_agenda(event_name: str, date: str, sessions: str):
    prompt = f"Generate an agenda for event '{event_name}' on {date} with sessions: {sessions}"
    return {"agenda": ask_gpt(prompt)}

@app.post("/calendar")
def calendar_event(title: str, start: str, end: str):
    event = create_event(title, start, end)
    return {"event_id": event['id']}

@app.get("/events")
def upcoming_events():
    return {"events": list_events()}

@app.post("/announce")
def announce(text: str):
    send_telegram_message(text)
    return {"status": "Message sent"}

import requests

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=payload)
    return response.status_code, response.text

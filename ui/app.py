# ui/app.py
import streamlit as st
import requests

st.title("Club Assistant")

option = st.selectbox("Choose Action", ["Draft Email", "Generate Agenda", "Create Event", "Post to Telegram"])

if option == "Draft Email":
    topic = st.text_input("Email Topic")
    if st.button("Generate"):
        res = requests.post("http://localhost:8000/email", params={"prompt": topic})
        st.text_area("Email", res.json()["email"])

elif option == "Generate Agenda":
    name = st.text_input("Event Name")
    date = st.date_input("Date")
    sessions = st.text_area("Sessions (comma-separated)")
    if st.button("Generate"):
        res = requests.post("http://localhost:8000/agenda", params={
            "event_name": name, "date": str(date), "sessions": sessions
        })
        st.text_area("Agenda", res.json()["agenda"])

elif option == "Create Event":
    title = st.text_input("Title")
    start = st.text_input("Start Time (e.g., 2025-05-01T10:00:00)")
    end = st.text_input("End Time")
    if st.button("Add"):
        res = requests.post("http://localhost:8000/calendar", params={"title": title, "start": start, "end": end})
        st.success(f"Event Created: {res.json()['event_id']}")

elif option == "Post to Telegram":
    msg = st.text_area("Message")
    if st.button("Send"):
        res = requests.post("http://localhost:8000/announce", params={"text": msg})
        st.success("Sent to Telegram!")

from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_PATH")
CALENDAR_ID = 'primary'

credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

def create_event(title, start_time, end_time):
    event = {
        'summary': title,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'}
    }
    return service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

def list_events():
    events_result = service.events().list(calendarId=CALENDAR_ID, maxResults=5, singleEvents=True, orderBy='startTime').execute()
    return events_result.get('items', [])

import requests

TOKEN = "7281056209:AAGuB36NThzsSRUX4U8_J1SPyd0n6JyVszk"  # Replace with your new token
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(URL)
print(response.status_code)
print(response.text)

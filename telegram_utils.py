import telepot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telepot.Bot(os.getenv("TELEGRAM_BOT_TOKEN"))
chat_id = os.getenv("CHAT_ID")

def send_telegram_message(text):
    bot.sendMessage(chat_id, text)

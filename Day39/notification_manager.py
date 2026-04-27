import requests
import os

class NotificationManager:
    def __init__(self):
        self.bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.environ.get("CHAT_ID")
        self.url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
    
    def send_message(self, message):
        tele_para = {
            "chat_id" : f"{self.chat_id}",
            "text" : message
        }
        tele_res = requests.get(url=self.url, params=tele_para)
        tele_res.raise_for_status()
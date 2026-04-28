import requests
import os
import smtplib

class NotificationManager:
    def __init__(self):
        self.bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.environ.get("CHAT_ID")
        self.url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        
    
    def send_message(self, message):
        tele_para = {
            "chat_id" : f"{self.chat_id}",
            "text" : message
        }
        tele_res = requests.get(url=self.url, params=tele_para)
        tele_res.raise_for_status()

    def send_emails(self, email_list, email_body):
        smtp_address = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")
        
        with smtplib.SMTP(smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(self.email, self.email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
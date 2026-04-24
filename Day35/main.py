import requests
import os

api_key = os.environ.get("OWM_API_KEY")

def send_telegram_msg(message):
    bot_token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    parameter = {
        "chat_id" : chat_id,
        "text" : message,
    }
    response = requests.get(url=url, params=parameter)
    response.raise_for_status()

parameters = {
    "lat" : 12.976794,
    "lon" : 77.590082,
    "appid" : api_key,
    "cnt": 4,
    }

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id0 = weather_data["list"][0]["weather"][0]["id"]
weather_id1 = weather_data["list"][1]["weather"][0]["id"]
weather_id2 = weather_data["list"][2]["weather"][0]["id"]
weather_id3 = weather_data["list"][3]["weather"][0]["id"]
weather_ids = [weather_id0, weather_id1, weather_id2, weather_id3]
for id in weather_ids:
    if id < 700:
        will_rain = True
if will_rain:
    send_telegram_msg("It will rain. Please carry an Umbrella.")

import requests
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_api = os.environ.get("ALPHA_API_KEY")

stock_para = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" : f"{alpha_api}"
}

   
stock_res = requests.get(url=STOCK_ENDPOINT, params=stock_para)
data = stock_res.json()
daily_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in daily_data.items()]
yesterday_data = data_list[0]
yesterday_close = float(yesterday_data["4. close"])



day_before_data = data_list[1]
day_before_close = float(day_before_data["4. close"])


pd = (yesterday_close) - (day_before_close)
up_down = "🔺" if pd > 0 else "🔻"
pos_diff = float(round(abs(pd), 2))
print(pos_diff)


percentage = round((pos_diff/day_before_close)*100, 2)
print(f"{percentage}%")



def get_news():
    global formatted_articles
    news_api = os.environ.get("NEWS_API")
    dates = [key for (key, value) in daily_data.items()] 
    last_marketday = dates[0]

    news_para = {
        "q" : COMPANY_NAME,
        "from" : last_marketday,
        "sortBy": "popularity",
        "apiKey": f"{news_api}"
    }
    news_res = requests.get(url=NEWS_ENDPOINT, params=news_para)
    news = news_res.json()
    articles = news["articles"][:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage}%\n\nHeadlines : {article['title']}\n\nBrief : {article['description']}" for article in articles]

def send_message():
    bot_token = os.environ.get("TOKEN_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    chat_id = os.environ.get("CHAT_ID")
    
    for article_message in formatted_articles:
        tele_para = {
            "chat_id" : f"{chat_id}",
            "text" : article_message
        }
        tele_res = requests.get(url=url, params=tele_para)
        tele_res.raise_for_status()


if percentage > 5:
    get_news()
    send_message()

    












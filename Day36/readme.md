# 📈 Stock News Alert System (TSLA)

A Python-based financial monitoring tool that tracks significant price movements in Tesla ($TSLA) stock and automatically broadcasts relevant news headlines via a Telegram Bot.

## 🚀 Overview
Built as part of the #100DaysOfCode journey, this project integrates stock market data with real-time news to provide actionable insights. When the stock price fluctuates by more than 2% between the two most recent trading days, the system fetches the top 3 news articles and delivers them directly to a mobile device.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **APIs:** Alpha Vantage (Market Data), NewsAPI (Global News), Telegram Bot API (Notifications)
- **Environment Management:** `python-dotenv` for secure credential handling
- **IDE:** Cursor AI

## 🧠 Key Engineering Features

### 1. Dynamic Date Extraction
Unlike static scripts, this system uses **List Comprehension** and **Dictionary Slicing** to handle the "Weekend Problem." 
- Instead of hardcoding dates, the script converts the API response into a list:
  `data_list = [value for (key, value) in daily_data.items()]`
- This ensures that index `[0]` and `[1]` always represent the two most recent active trading days, making the code immune to market holidays and weekends.

### 2. Environment Security
Sensitive credentials (API Keys, Token IDs, Chat IDs) are managed through a `.env` file, ensuring no secrets are ever leaked to public repositories.

### 3. Automated Notification Pipeline
The system formats headlines and briefs into a clean, aesthetic Telegram message, utilizing emojis to indicate price direction (🔺/🔻) and percentage change.

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/stock-news-alert.git](https://github.com/yourusername/stock-news-alert.git)

2. Install dependencies::
    pip install requests python-dotenv

3. Create a .env file in the root directory and add your keys:
    ALPHA_API_KEY=your_alpha_vantage_key
    NEWS_API=your_news_api_key
    TOKEN_ID=your_telegram_bot_token
    CHAT_ID=your_telegram_chat_id

4. Run the script:
    python main.py
    
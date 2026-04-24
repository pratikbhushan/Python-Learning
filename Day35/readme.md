# Voyager: Automated Rain Alert System ☔️

A Python-based utility that monitors real-time weather data and delivers instant rain notifications via the Telegram Bot API. This project focuses on API integration, JSON parsing, and secure credential management.

## 📌 Project Overview
Voyager is designed to solve a simple problem: forgetting an umbrella. It queries the OpenWeatherMap API to analyze the forecast for the next 12 hours. If any precipitation (rain, snow, or storms) is detected, the system automatically triggers a push notification to a private Telegram bot.

## 🚀 Key Features
* **Predictive Analysis:** Specifically monitors the next four 3-hour forecast blocks (12-hour window).
* **Telegram Integration:** Uses a custom Telegram bot to deliver free, real-time mobile alerts.
* **Security-First Design:** Implements the `os` module to fetch credentials from environment variables, ensuring no API keys are hardcoded.
* **Industrial Weather Logic:** Uses OpenWeatherMap condition codes (IDs < 700) to accurately identify all forms of inclement weather.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **API Interactions:** `requests` library
* **Environment Management:** `os` module (System-level environment variables)
* **Data Format:** JSON

## ⚙️ Setup & Installation

### 1. Prerequisites
You will need an API key from [OpenWeatherMap](https://openweathermap.org/) and a Telegram Bot token from [@BotFather](https://t.me/botfather).

Install the required library:
```bash
pip install requests
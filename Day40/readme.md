# Flight Price Tracker

An automated flight intelligence system that monitors price arbitrage for domestic and international routes. Version 2.0 introduces a multi-user notification system, a subscriber database, and intelligent fallback logic for indirect flight routes.

---

##  Architecture Overview

The system follows a decoupled, Object-Oriented (OOP) architecture. Here is how the components interact:

```text
Flight Price Tracker Architecture
├── 1. Database Layer (Google Sheets via Sheety API)
│   ├── Read: Fetches Watchlist (Destinations & Target Prices)
│   └── Write: Updates missing IATA codes & new "Record Low" prices
│
├── 2. Core Execution Engine (Python)
│   ├── main.py (Orchestrator: loops through destinations and logic)
│   ├── data_manager.py (Handles all RESTful HTTP requests to Sheety)
│   ├── flight_search.py (Connects to Amadeus/SerpAPI/Kiwi for live data)
│   └── flight_data.py (Data Transfer Object: parses and structures JSON)
│
└── 3. Alerting Layer (Telegram API & SMTP)
    └── notification_manager.py (Manages secure SMTP (Email) and Telegram alerts.)


Google Sheets (Database)          Telegram / Email
          ^                               |
          | REST (Sheety API)             | Outbound Alert
          v                               v
    ┌──────────────────────────────────────────────┐
    |                Core Engine                   |
    |  ┌────────────┐  ┌────────────┐  ┌─────────┐ |
    |  | DataManager|  |FlightSearch|  | Notify  | |
    |  | (CRUD)     |  | (API)      |  | Manager | |
    |  └─────┬──────┘  └─────┬──────┘  └────┬────┘ |
    |        |               |              |      |
    |  ┌─────v───────────────v──────────────v────┐ |
    |  |            Execution Layer              | |
    |  |      IATA Fetching | Price Parsing      | |
    |  └─────────────────────┬───────────────────┘ |
    └────────────────────────|─────────────────────┘
                             v
                    Flight Search API
                         (SerpAPI)
```
---

## ✨ Key Features

* **Intelligent Fallback Logic:** If a direct flight is unavailable or above the target price, the engine automatically re-scans the market for indirect flights with stopover capabilities.
* **Multi-User Notification System:** Dynamically fetches a list of subscribers from the database and dispatches personalized email alerts to all users simultaneously.
* **Smart Stopover Detection:** Captures and reports the number of stops in the alert message, ensuring transparency for travel planning.
* **Performance Caching:** Integrated `requests-cache` with an SQLite backend to minimize redundant API calls and optimize rate-limit usage.
* **Automated Data Integrity:** Programmatically identifies missing IATA codes and updates the Google Sheet via RESTful PUT requests.
---

## 🛠 Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Database** | Google Sheets (via Sheety API) |
| **APIs** | SerpAPI |
| **Notifications** | Telegram Bot API & smtplib (TLS/SSL) |
| **Caching** | requests-cache (SQLite) |
| **Environment** | Python-Dotenv (Secrets Management) |

---

## 📂 Project Structure

```text
├── main.py                  # Orchestration logic and main execution loop
├── data_manager.py          # Google Sheets CRUD operations (Sheety API)
├── flight_search.py         # API integration for flight price retrieval
├── flight_data.py           # Data structuring and JSON parsing logic
├── notification_manager.py  # Telegram/Email alerting service
├── .env                     # Private API keys and credentials (hidden)
├── .gitignore               # Prevents secrets and cache leakage to GitHub
└── requirements.txt         # Project dependencies

```
## 🚀 Getting Started


Follow these step-by-step instructions to set up the tracker on your local machine.

### 1. Prerequisites
* **Python 3.11+** installed on your system.
* A **A Google Sheet with two tabs:** prices (City, IATA Code, Lowest Price) and users (First Name, Last Name, Email).
* A **Gmail App Password** (Generated via Google Account > Security > 2-Step Verification).
* API credentials for **Sheety**, your chosen **Flight Search provider** (e.g., SerpAPI), and a **Telegram Bot**.

### 2. Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/pratikbhushan/flight-price-tracker.git
cd flight-price-tracker
pip install -r requirements.txt

```
### 3. Configuration
Create a .env file in the root directory to securely store your API keys. (Ensure .env is listed in your .gitignore file so it doesn't get uploaded to GitHub).

SHEETY_ENDPOINT=https://api.sheety.co/your_id/project/prices
SHEETY_TOKEN=your_secret_token
FLIGHT_API_KEY=your_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_16_digit_app_password
EMAIL_PROVIDER_SMTP_ADDRESS=smtp.gmail.com

### 4. Execution
Run the orchestrator script to start tracking:

```bash
python main.py

```
## ⚙️ How It Works

The system operates in a continuous, automated loop broken down into five distinct phases:

### 1. Synchronization
Fetches the destination watchlist and the user email list from Google Sheets.

### 2. Market Scanning
Searches for direct flights from the origin (e.g., BLR) within a 6-month window.

### 3. Fallback Sequence
If no direct flights are found (N/A), the `main.py` orchestrator triggers an indirect search allowing 1+ stops.

### 4. Verification
Compares the best market price found against the "Lowest Price" threshold in the database.

### 5. Action & Alerting
If a deal is detected, the `DataManager` updates the record low in the sheet, and the NotificationManager sends a formatted alert to both the `Telegram bot` and every email in the subscriber list.


## 📜 License

Proprietary. Developed as a python learning project. All rights reserved.
# Flight Price Tracker

An automated flight intelligence engine that monitors price arbitrage for domestic and international routes, providing real-time alerts when ticket costs drop below user-defined thresholds.

---

##  Architecture Overview

The system follows a decoupled, Object-Oriented (OOP) architecture. Here is how the components interact:


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
└── 3. Alerting Layer (Telegram API)
    └── notification_manager.py (Formats and pushes mobile alerts)


Google Sheets (Database)          Telegram / SMS
          ^                               |
          | REST (Sheety API)             | Outbound Alert
          v                               v
    ┌──────────────────────────────────────────────┐
    |                Vayu Core Engine              |
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

---

## ✨ Key Features

* **Automated IATA Resolution:** Programmatically identifies missing airport codes (e.g., "Patna" → "PAT") and updates the database via RESTful PUT requests.
* **Dynamic Price Comparison:** Implements logic to compare real-time market rates against "Target Prices" stored in the spreadsheet.
* **Intelligent Alerting:** Triggers instant notifications via Telegram only when a genuine price drop is detected, avoiding notification fatigue.
* **Performance Caching:** Integrated `requests-cache` with an SQLite backend to minimize redundant API calls and optimize rate-limit usage.
* **Rolling Search Window:** Automatically calculates a 6-month search window from the current execution date to find the best mid-term travel deals.

---

## 🛠 Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Database** | Google Sheets (via Sheety API) |
| **APIs** | SerpAPI |
| **Notifications** | Telegram Bot API |
| **Caching** | requests-cache (SQLite) |
| **Environment** | Python-Dotenv (Secrets Management) |

---

## 📂 Project Structure

```text
├── main.py                  # Orchestration logic and main execution loop
├── data_manager.py          # Google Sheets CRUD operations (Sheety API)
├── flight_search.py         # API integration for flight price retrieval
├── flight_data.py           # Data structuring and JSON parsing logic
├── notification_manager.py  # Telegram/SMS alerting service
├── .env                     # Private API keys and credentials (hidden)
├── .gitignore               # Prevents secrets and cache leakage to GitHub
└── requirements.txt         # Project dependencies


## 🚀 Getting Started

Follow these step-by-step instructions to set up the tracker on your local machine.

### 1. Prerequisites
* **Python 3.11+** installed on your system.
* A **Google Sheet** configured with your Sheety account. It must have these exact columns: `City`, `IATA Code`, and `Lowest Price`.
* API credentials for **Sheety**, your chosen **Flight Search provider** (e.g., SerpAPI), and a **Telegram Bot**.

### 2. Installation
Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/yourusername/flight-price-tracker.git](https://github.com/yourusername/flight-price-tracker.git)
cd flight-price-tracker
pip install -r requirements.txt


### 3. Configuration
Create a .env file in the root directory to securely store your API keys. (Ensure .env is listed in your .gitignore file so it doesn't get uploaded to GitHub).

SHEETY_ENDPOINT=[https://api.sheety.co/your_id/project/prices](https://api.sheety.co/your_id/project/prices)
SHEETY_TOKEN=your_secret_token
FLIGHT_API_KEY=your_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

### 4. Execution
Run the orchestrator script to start tracking:

```bash
python main.py


## ⚙️ How It Works

The system operates in a continuous, automated loop broken down into five distinct phases:

### 1. Synchronization
The `DataManager` initiates a GET request to the Google Sheet to pull the current watchlist of destinations and their target prices. If the system detects any missing IATA airport codes (e.g., a user typed "Patna" but left the code blank), the `FlightSearch` module automatically resolves the correct code and updates the sheet.

### 2. Market Scanning
The core engine iterates through the synchronized destination list. For each city, it queries the flight search API to find the absolute cheapest outbound and return flights departing from the origin city (e.g., BLR) within a rolling 6-month window.

### 3. Data Parsing
Raw JSON responses from flight APIs are highly complex. The `FlightData` object acts as a parser, traversing the nested dictionaries to extract only the necessary variables: the lowest price, departure/arrival airport codes, and specific travel dates.

### 4. Verification
The engine runs a strict comparison logic. It evaluates the freshly parsed market price against the "Lowest Price" threshold currently stored for that specific city in the Google Sheet.

### 5. Action & Alerting
If the market price is strictly lower than the threshold, the system triggers a dual-action sequence:
* **Database Update:** The `DataManager` sends a PUT request to the Google Sheet, overwriting the old price with the new "Record Low."
* **Instant Alert:** The `NotificationManager` dispatches a formatted Telegram message directly to the user's phone, detailing the price drop and travel dates so they can book immediately.


## 📜 License

Proprietary. Developed as a python learning project. All rights reserved.
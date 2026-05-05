# Amazon Price Tracker

A professional-grade Python automation script that monitors Amazon product prices and sends automated email alerts when a target price threshold is met.

## Features
*   **Real-time Scraping:** Extracts live price data using BeautifulSoup4.
*   **Automated Notifications:** Sends structured email alerts via SMTP.
*   **Anti-Detection:** Uses custom HTTP headers to bypass automated bot detection.
*   **Secure:** Manages sensitive credentials (emails, passwords) through environment variables.

## Built With
*   **Python 3.13**
*   **Requests:** For handling HTTP network calls.
*   **BeautifulSoup4:** For parsing and navigating HTML.
*   **smtplib:** For email transmission.
*   **python-dotenv:** For secure configuration management.

## Quick Start

### 1. Prerequisites
Ensure you have Python installed. Install the required libraries using:
```bash
pip install requests beautifulsoup4 python-dotenv
```

### 2. Configuration
Create a file named .env in the same folder as your code and paste the following, replacing the values with your actual details:
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_sending_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
TO_EMAIL=your_receiving_email@gmail.com

### 3. Usage
Simply run the script. It will check the price, compare it to your target, and send an email if a deal is found.
```bash
python main.py
```

## LOGIC OVERVIEW: AMAZON PRICE TRACKER

1. **REQUEST PHASE:**
   The script uses the 'requests' library to fetch the raw HTML data 
   from the specified Amazon India URL. It sends a custom header 
   (User-Agent and Accept-Language) to mimic a real browser and 
   avoid being blocked as a bot.

2. **SCRAPING PHASE:**
   BeautifulSoup parses the HTML response. It specifically looks for:
   - The 'aok-offscreen' class to find the most accurate current price.
   - The 'productTitle' ID to grab the full name of the item.

3. **DATA PROCESSING PHASE:**
   - It captures the price string (e.g., "₹189.00").
   - It splits the string to remove the currency symbol and extra text.
   - It converts the remaining string into a 'float' data type so Python 
     can perform a mathematical comparison.

4. **TRIGGER PHASE:**
   The script compares 'split_price' against 'target_price'. 
   If the current price is lower than the target:
   - It constructs a notification message with the product title.
   - It connects to Gmail's SMTP server via port 587.
   - It secures the connection using TLS encryption.
   - It logs in and sends the alert email with UTF-8 encoding.
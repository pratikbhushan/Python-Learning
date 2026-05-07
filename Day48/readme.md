# AUTOMATED COOKIE CLICKER BOT

A high-speed automation script built with Python and Selenium to play the official Cookie Clicker game. The bot handles initial setup, rapid clicking, and implements a smart purchasing strategy.

## 📌 PROJECT OVERVIEW
This bot automates the first 5 minutes of gameplay. It executes a continuous click loop on the big cookie and pauses every 5 seconds to check the in-game economy to buy production-boosting upgrades.

## 🛠️ FEATURES
- Dynamic Waiting: Uses WebDriverWait to handle the "Language Selection" splash screen.
- High-Speed Clicking: Uses a Python loop to click the cookie as fast as the CPU allows.
- Checkpoint Logic: Uses a temporal checkpoint method (time.time()) to manage shopping without stopping the clicking.
- Data Sanitization: Handles the "1,000" comma formatting to convert string counts into integers.
- Resilient Error Handling: Uses try/except blocks to prevent crashes during purchase attempts.

## 📋 PREREQUISITES
- Python 3.x installed.
- Selenium library installed.
- Chrome browser installed.

## 🚀 INSTALLATION & SETUP
1. Install Selenium using the terminal:
   pip install selenium

2. Ensure your Chrome browser is updated.

3. Save the script as 'cookie_bot.py'.

## 🎮 HOW TO RUN
Run the script through your terminal or IDE:
python cookie_bot.py

## 📝 LOGIC OVERVIEW
1. INITIALIZATION: Launches Chrome in 'detach' mode so the window stays open after the bot finishes.
2. LANGUAGE SELECT: The bot waits up to 15 seconds for the English language button (ID: langSelect-EN) to become clickable.
3. THE 5-MINUTE TIMER: Sets a 'timeout' variable for 300 seconds.
4. THE CLICK ENGINE: Rapidly clicks the 'bigCookie' element.
5. THE SHOPPING CYCLE: Every 5 seconds, the bot:
   - Scrapes the current cookie count.
   - Removes commas (e.g., "1,250" becomes 1250).
   - If cookies >= 100: Buys a Grandma (product1).
   - If cookies >= 15: Buys a Cursor (product0).

## 🤝 CONTRIBUTIONS
Feel free to fork this project to add more complex features, such as:
- Scraping actual price tags instead of hard-coded values.
- Implementing an ROI algorithm to buy the most efficient upgrade.
- Adding a CSV logger for cookie production stats.
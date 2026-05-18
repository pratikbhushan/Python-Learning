# Zillow Data Entry Automation Bot

An automated Python bot that scrapes rental property data from a Zillow clone website and automatically fills a Google Form using Selenium.

This project combines:

- Web Scraping with BeautifulSoup
- HTTP Requests using Requests
- Browser Automation using Selenium
- Automated Form Submission

---

## 🚀 Features

- Scrapes:
  - Property Prices
  - Property Addresses
  - Property Links
- Automatically opens Google Forms
- Fills form fields dynamically
- Submits multiple responses automatically
- Simulates a real-world data entry automation workflow

---

## 🛠️ Tech Stack

- Python
- Selenium
- BeautifulSoup4
- Requests
- ChromeDriver

---

## 📂 Project Structure

```bash
.
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zillow-data-entry-bot.git
cd zillow-data-entry-bot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install selenium beautifulsoup4 requests
```

---

### 3. Install ChromeDriver

Download ChromeDriver matching your Chrome version:

https://chromedriver.chromium.org/downloads

Add it to your PATH.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Scrape rental listings from the Zillow Clone website
2. Extract:
   - Price
   - Address
   - Property Link
3. Open the Google Form
4. Automatically fill and submit entries

---

## 📸 Workflow

```text
Zillow Clone Website
        ↓
Scrape Listing Data
        ↓
Store Data in Lists
        ↓
Open Google Form
        ↓
Fill Inputs Automatically
        ↓
Submit Response
        ↓
Repeat
```

---

## 🧠 Concepts Practiced

This project demonstrates:

- HTML Parsing
- Web Scraping
- XPath Selectors
- Selenium Automation
- Dynamic Web Interaction
- Data Extraction
- Form Automation

---

## ⚠️ Important Notes

- This project uses a Zillow Clone website from App Brewery for educational purposes.
- Google Form structure may change over time, which can break XPath selectors.
- Make sure ChromeDriver version matches your installed Chrome browser.

---

## 🔧 Possible Improvements

- Add Exception Handling
- Use Explicit Waits everywhere instead of `time.sleep()`
- Store data in CSV/JSON
- Headless Browser Support
- Randomized Delays for Human-like Behavior
- Deploy using Docker
- Add Logging System

---

## 🐞 Known Limitations

- Hardcoded XPath selectors
- Assumes exactly 44 entries
- May fail if page structure changes
- Slow due to browser automation

---

## 📚 Learning Outcomes

By building this project, you learn:

- Real-world automation workflows
- Browser automation fundamentals
- How websites structure HTML
- Practical Selenium usage
- Combining scraping + automation together

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is for educational purposes only.

---

## ⭐ Acknowledgements

- App Brewery
- Selenium Documentation
- BeautifulSoup Documentation
- Zillow Clone Project
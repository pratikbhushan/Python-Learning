# 🏋️ Gym Class Auto Booker

An automated gym class booking bot built with Python and Selenium.

This script automatically:

- Logs into your gym portal
- Finds Tuesday & Thursday 6:00 PM classes
- Books available classes
- Joins waitlists if classes are full
- Verifies bookings from the "My Bookings" page
- Uses retry logic for stability and reliability

---

# 🚀 Features

✅ Automatic login using environment variables  
✅ Persistent Chrome profile (stays logged in)  
✅ Smart retry system for unstable page loads  
✅ Auto booking for specific days & times  
✅ Auto waitlisting when classes are full  
✅ Booking verification system  
✅ Clean console logs for tracking actions  

---

# 📂 Project Structure

```bash
.
├── main.py
├── .env
└── chrome_profile/
```

---

# ⚙️ Requirements

- Python 3.10+
- Google Chrome
- ChromeDriver installed

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/gym-class-auto-booker.git
cd gym-class-auto-booker
```

---

## 2. Install dependencies

```bash
pip install selenium python-dotenv
```

---

## 3. Create a `.env` file

```env
ACCOUNT_EMAIL=your_email_here
ACCOUNT_PASSWORD=your_password_here
GYM_URL=https://yourgymwebsite.com
```

---

# ▶️ Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Open Chrome
2. Login automatically
3. Search for Tuesday/Thursday 6PM classes
4. Book or waitlist classes
5. Verify all successful bookings

---

# 🧠 How It Works

## Login System

The script uses Selenium to:

- Open the gym website
- Click login
- Enter credentials
- Navigate to the schedule page

---

## Booking Logic

The bot scans all available class cards and filters:

- Tuesday classes
- Thursday classes
- 6:00 PM timings

Then it:

- Books available classes
- Joins waitlists if full
- Skips already booked classes

---

## Retry Mechanism

A custom retry function improves reliability during:

- Slow page loads
- Temporary timeouts
- Unstable UI interactions

```python
def retry(func, retries=7, description=None):
```

---

## Verification System

After booking, the bot:

- Opens the "My Bookings" page
- Confirms every expected booking exists
- Detects mismatches automatically

---

# 🛡️ Environment Variables

| Variable | Description |
|---|---|
| `ACCOUNT_EMAIL` | Gym account email |
| `ACCOUNT_PASSWORD` | Gym account password |
| `GYM_URL` | Gym booking portal URL |

---

# 🔥 Example Console Output

```bash
Trying login. Attempt: 1
✓ Successfully booked: Yoga on Tue
✓ Joined waitlist for: HIIT on Thu

--- VERIFICATION RESULT ---
Expected: 2 bookings
Found: 2 bookings

✅ SUCCESS: All bookings verified!
```

---

# 🧩 Technologies Used

- Python
- Selenium
- Chrome WebDriver
- python-dotenv

---

# ⚠️ Notes

- The script uses a persistent Chrome profile to avoid repeated logins.
- Ensure ChromeDriver version matches your Chrome browser version.
- The booking system depends on the website structure and element IDs remaining unchanged.

---

# 📌 Future Improvements

- Email/Discord notifications
- Headless browser support
- Multi-time-slot support
- Automatic scheduling with cron jobs
- Docker support
- GUI dashboard

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Built by Pratik 🚀
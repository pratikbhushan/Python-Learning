import requests
import smtplib
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

URL = "https://www.amazon.in/Oblivion-Buddha-Monk-Figurines-Set/dp/B0DS2HF6L7/ref=s9_acsd_al_ot_cv2_5_t?_encoding=UTF8&pf_rd_t="
SMTP_ADD = os.environ.get("SMTP_ADDRESS")
EMAIL = os.environ.get("EMAIL_ADDRESS")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
HEADER = {"User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0", "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(url=URL, headers=HEADER)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
whole_price = soup.find(name="span", class_="aok-offscreen").getText()
split_price = float(whole_price.split()[0].split("₹")[1])

target_price = float(200)

title = soup.find(name="span", id = "productTitle", class_="a-size-large product-title-word-break").getText()


if split_price < target_price:
    message = f"{title} is on sale for {whole_price}!"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail( from_addr=EMAIL,
            to_addrs=os.environ["TO_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )

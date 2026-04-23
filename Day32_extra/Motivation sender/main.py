import smtplib
import random
import datetime as dt

my_email = "eclipsevoyagerx@gmail.com"
password = "zjta nbzs pasg dtcu"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open(r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day32\Motivation sender\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="pratikbhushan13@gmail.com", 
            msg=f"Subject:Monday Motivation\n\n{quote}")    
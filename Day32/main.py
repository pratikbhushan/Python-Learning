import datetime as dt
import pandas
import smtplib
import random

username = "eclipsevoyagerx@gmail.com"
password = ""


now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv(r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day32\birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path1 = r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day32\letter_templates\letter_1.txt"
    file_path2 = r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day32\letter_templates\letter_2.txt"
    file_path3 = r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day32\letter_templates\letter_3.txt"
    file_list = [file_path1, file_path2, file_path3]
    one_file = random.choice(file_list)
    with open(one_file) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{new_content}")

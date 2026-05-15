from selenium import webdriver
from selenium.webdriver.common.by import By
from InstaFollower import instafollower
import os 
from dotenv import load_dotenv

load_dotenv()


USERNAME = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
SIMILAR_ACC = os.environ.get("SIMILAR_ACCOUNT")
ins_bot = instafollower()

login = ins_bot.login(user=f"{USERNAME}", password=f"{PASSWORD}")

finder = ins_bot.find_followers(similar=SIMILAR_ACC)

follow = ins_bot.follow()


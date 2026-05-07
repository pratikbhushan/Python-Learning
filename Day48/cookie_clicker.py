from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


wait = WebDriverWait(driver, 15)
try:
    language_btn = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
    language_btn.click()
    print("Language Selected: English")
except Exception as e:
    print("Language button didn't appear or was already selected.")

time.sleep(2)


cookie = driver.find_element(By.ID, value='bigCookie')

start_time = time.time()
five_sec_checkpoint = time.time() + 5
timeout = time.time() + 60 * 5  

print("Bot is clicking... Watch the store every 5 seconds!")

while time.time() < timeout:
    cookie.click()

    if time.time() > five_sec_checkpoint:
        
        raw_count = driver.find_element(By.ID, value='cookies').text.split()[0]
        cookie_num = int(raw_count.replace(",", ""))
        
        try:
            if cookie_num >= 100:
                driver.find_element(By.ID, value='product1').click()
            elif cookie_num >= 15:
                driver.find_element(By.ID, value='product0').click()
        except:
            pass

        five_sec_checkpoint = time.time() + 5

print("Game Over. Your cookie empire is established.")
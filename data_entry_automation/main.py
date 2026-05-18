import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.content, "html.parser")

price_list = []
link_list = []
address_list = []

prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

for price in prices:
    price_list.append(price.text.split("+")[0].split("/")[0])

print(price_list)

links = soup.find_all(class_ = "StyledPropertyCardDataArea-anchor")

for link in links:
    link_list.append(link.get('href'))
    print(link_list)

addresses = soup.find_all("address")

for address in addresses:
    address_list.append(address.text.split("\n")[1].split("                                  ")[1])

    print(address_list)

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeoptions)

driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSdz0uWzzjhIY8GFuoVprTY0d2opy5X6M7RR39ZuKht8QKS0UA/viewform?usp=header")


def filler(n):

    time.sleep(5)

    inputs = driver.find_elements(
        By.XPATH,
        "//input[@type='text']"
    )

    print(f"Found {len(inputs)} text inputs")

    inputs[0].send_keys(address_list[n])

    inputs[1].send_keys(price_list[n])

    inputs[2].send_keys(link_list[n])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    another_response_button = WebDriverWait(driver, 2).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    another_response_button.click()

for n in range(44):
    filler(n)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

class instafollower:
    def __init__(self):
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chromeoptions)
        self.driver.maximize_window()

        self.driver.get("https://www.instagram.com/")

    def login(self, user, password):
        username_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']"))
        )
        username_button.clear()
        username_button.send_keys(user)

        password_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']"))
        )
        password_button.clear()
        password_button.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button.click()

        save_info_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()='Save info']"))
        )
        save_info_button.click()

        notification_button = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        notification_button.click()

    def find_followers(self, similar):
        size = self.driver.get_window_size()

        width = size['width']
        height = size['height']

        print(f"Window size: {width}x{height}")

        actions = ActionChains(self.driver)
        body = self.driver.find_element(By.TAG_NAME, "body")
        actions.move_to_element_with_offset(body, -751, 20).perform()
        
        time.sleep(2)

        search_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//span[text()='Search']"))
        )
        search_button.click()

        search_box = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//input[@aria-label='Search input']"))
        )
        search_box.send_keys(similar)

        account_clicker = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/virat.kohli/']"))
        )
        account_clicker.click()

        followers_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//span[text()=' followers']"))
        )
        followers_button.click()

    def follow(self):

        WebDriverWait(self.driver, 15).until(
            ec.presence_of_element_located(
                (By.XPATH, "//*[text()='Follow']")
            )
        )

        for i in range(6):

            follow_buttons = self.driver.find_elements(
                By.XPATH,
                "//*[text()='Follow']"
            )

            print(f"Found {len(follow_buttons)} buttons")

            if len(follow_buttons) == 0:
                break

            button = follow_buttons[0]

            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);",
                button
            )

            time.sleep(2)

            ActionChains(self.driver)\
                .move_to_element(button)\
                .pause(1)\
                .click()\
                .perform()

            print("Clicked")

            time.sleep(3)
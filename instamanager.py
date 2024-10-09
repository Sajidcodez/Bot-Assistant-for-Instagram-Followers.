from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

class InstaManager:
    
    def __init__(self, driver):
        self.driver = driver

    def unfollow_everyone(self, username):
        # Go to the user's Instagram profile
        self.driver.get(f"https://www.instagram.com/{username}/")

        time.sleep(3)
        # Click on the "Following" list
        following_button = self.driver.find_element(By.XPATH, "//a[contains(@href,'/following')]")
        following_button.click()

        time.sleep(5)
        # Loop through and click "Unfollow" on all followed accounts
        while True:
            unfollow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")

            if len(unfollow_buttons) == 0:
                break

            for button in unfollow_buttons:
                if button.text == "Following" or button.text == "Requested":
                    try:
                        button.click()
                        time.sleep(1.5)
                        confirm_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Unfollow')]")
                        confirm_button.click()
                        time.sleep(2)
                    except ElementClickInterceptedException:
                        cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                        cancel_button.click()
                        time.sleep(1)

    def remove_all_followers(self, username):
        # Go to the user's Instagram profile
        self.driver.get(f"https://www.instagram.com/{username}/")

        time.sleep(3)
        # Click on the "Followers" list
        followers_button = self.driver.find_element(By.XPATH, "//a[contains(@href,'/followers')]")
        followers_button.click()

        time.sleep(5)
        # Loop through and click "Remove" for all followers
        while True:
            remove_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Remove']")

            if len(remove_buttons) == 0:
                break

            for button in remove_buttons:
                try:
                    button.click()
                    time.sleep(1.5)
                    confirm_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]")
                    confirm_button.click()
                    time.sleep(2)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                    time.sleep(1)

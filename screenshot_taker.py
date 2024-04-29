from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
import time


class ScreenshotTaker:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def take_screenshot(self, urls, output_folder):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"webdriver.chrome.driver={self.driver_path}")

        # Create folder 

        for index,url in enumerate(urls): 

            url_folder = os.path.join(output_folder,url.split('//')[1])
            os.makedirs(url_folder,exist_ok=True)

            driver = webdriver.Chrome(options = chrome_options)

            driver.get(url) 

            try:
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,'body')))
                print(f"Page loaded successfully for url : {url}")
            except TimeoutException:
                print(f"Timeout occuresd while waiting for pate to load for url : {url}")
                continue
            
            screenshot_path = os.path.join(url_folder,f'screenshot_{index}.png')

            driver.save_screenshot(screenshot_path)

        driver.quit()


if __name__ == "__main__":
    # This file is intended to be imported by `main.py`
    pass
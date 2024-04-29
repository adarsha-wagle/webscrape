import time
from screenshot_taker import ScreenshotTaker

if __name__ == "__main__":
    # Example usage
    driver_path = 'chromedriver.exe'
    urls = ['https://example.com','https://d3fend.mitre.org/','https://aarohasoft.com']
    output_folder = 'screenshots'

    # Take screenshot 
    screenshot_taker = ScreenshotTaker(driver_path)
    screenshot_taker.take_screenshot(urls, output_folder)

import math
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BROWSER_HEIGHT = 1027

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://nomadcoders.co")
browser.maximize_window()

sizes = [480, 960, 1366, 1920]

for size in sizes:
    browser.set_window_size(size, BROWSER_HEIGHT)
    time.sleep(3)

    scroll_size = browser.execute_script("return document.body.scrollHeight")
    total_section = math.ceil(scroll_size / BROWSER_HEIGHT)
    for section in range(total_section):
        browser.execute_script(
            f"window.scrollTo(0, {(section) * BROWSER_HEIGHT})")
        time.sleep(2)

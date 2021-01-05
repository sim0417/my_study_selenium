import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from util import make_dir

url = "https://www.instagram.com/explore/tags/"
tag = "dog"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url + tag)

header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
hashtags = header.find_element_by_class_name("AC7dP")

for hashtag in hashtags:
    hashtag.click()

time.sleep(3)
browser.quit()


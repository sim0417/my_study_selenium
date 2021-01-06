import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from util import make_dir

url = "https://www.instagram.com/explore/tags/"
start_tag = "dog"
max_hastags = 15
counted_hastags = []
used_hastags = []

browser = webdriver.Chrome(ChromeDriverManager().install())

def wait_for(locator, duration = 10):
    return WebDriverWait(browser, duration).until(EC.presence_of_element_located(locator))

def clean_hashtag(hashtag):
    return hashtag[1:]

def extract_data():
    hashtag_name = wait_for((By.TAG_NAME, "h1"), 10)
    post_count = wait_for((By.CLASS_NAME, "g47SY"), 10)
    if post_count:
        post_count = int(post_count.text.replace(",",""))
    
    if hashtag_name:
        hashtag_name = clean_hashtag(hashtag_name)

    if hashtag_name and post_count:
        if hashtag_name not in used_hastags:
            counted_hastags.append((hashtag_name, post_count))
            used_hastags.append(hashtag_name)

def get_related(target_url):
    browser.get(target_url)
    header = wait_for((By.TAG_NAME, "header"), 10)
    hashtags = header.find_element_by_class_name("AC7dP")

    for hashtag in hashtags:
       hashtag_name = clean_hashtag(hashtag.text)
       if hashtag_name not in used_hastags:
           ActionChains(browser).key_down(Keys.COMMAND).click(hashtag).perform()


    for window in browser.window_handles:
        browser.switch_to.window(window)
        extract_data()
        time.sleep(1)

    if len(used_hastags) < max_hastags:
        for window in browser.window_handles:
            browser.switch_to.window(window)
            browser.close()
        browser.switch_to.window(browser.window_handles[0])
        get_related(browser.current_url)


get_related(url + start_tag)
print(counted_hastags) 

file = open(f"{start_tag}-report.csv", "w")
writer = csv.writer(file)
writer.writerow(["Hashtag", "Post Count"])

for hashtag in counted_hastags:
    writer.writerow(hashtag)

browser.quit()
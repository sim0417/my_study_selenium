import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Instaminer:
    def __init__(self, start_tag, max_hashtags):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "https://www.instagram.com/explore/tags/"
        self.start_tag = start_tag
        self.max_hastags = max_hashtags
        self.counted_hastags = []
        self.used_hastags = []
        
    def wait_for(self, locator, duration = 10):
        return WebDriverWait(self.browser, duration).until(EC.presence_of_element_located(locator))

    def clean_hashtag(self, hashtag):
        return hashtag[1:]

    def save_csv(self):
        file = open(f"{self.start_tag}-report.csv", "w")
        writer = csv.writer(file)
        writer.writerow(["Hashtag", "Post Count"])

        for hashtag in self.counted_hastags:
            writer.writerow(hashtag)

    def start(self):
        self.get_related(self.url + self.start_tag)

    def extract_data(self):
        hashtag_name = self.wait_for((By.TAG_NAME, "h1"), 10)
        post_count = self.wait_for((By.CLASS_NAME, "g47SY"), 10)
        if post_count:
            post_count = int(post_count.text.replace(",",""))
        
        if hashtag_name:
            hashtag_name = self.clean_hashtag(hashtag_name)

        if hashtag_name and post_count:
            if hashtag_name not in self.used_hastags:
                self.counted_hastags.append((hashtag_name, post_count))
                self.used_hastags.append(hashtag_name)

    def get_related(self, target_url):
        self.browser.get(target_url)
        header = self.wait_for((By.TAG_NAME, "header"), 10)
        hashtags = header.find_element_by_class_name("AC7dP")

        for hashtag in hashtags:
            hashtag_name = self.clean_hashtag(hashtag.text)
            if hashtag_name not in self.used_hastags:
                ActionChains(self.browser).key_down(Keys.COMMAND).click(hashtag).perform()

        for window in self.browser.window_handles:
            self.browser.switch_to.window(window)
            self.extract_data()
            time.sleep(1)

        if len(self.used_hastags) < self.max_hastags:
            for window in self.browser.window_handles:
                self.browser.switch_to.window(window)
                self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
            self.get_related(self.browser.current_url)
        else:
            self.browser.quit()
            self.save_csv()


Instaminer("dog", 15).start()
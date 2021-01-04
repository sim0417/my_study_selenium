import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from util import make_dir

url = "https://www.instagram.com/explore/tags/"
tag = "dog"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url + tag)

time.sleep(3)
browser.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

url = "https://repl.it/login"
xpath_id = "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/div[1]/div/div/input"
xpath_pwd = "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/div[2]/div/div/div/input"
class_login = "jsx-2671346692"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

username_input = browser.find_element_by_xpath(xpath_id)
password_input = browser.find_element_by_xpath(xpath_pwd)
login_btn = browser.find_element_by_class_name(class_login)

username_input.send_keys("sim0417")
password_input.send_keys(input("input password"))
login_btn.click()
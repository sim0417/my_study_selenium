from logging import setLogRecordFactory
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleSearchResultScreenshooter:
    def __init__(self, keyword, save_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.save_dir = save_dir

    def start(self):
        self.browser.get('https://google.com')
        search_input = self.browser.find_element_by_class_name('gLFyf')
        search_input.send_keys(self.keyword)
        search_input.send_keys(Keys.ENTER)

        self.delete_relation_element()

        search_results = self.browser.find_elements_by_class_name('g')

        for idx, result in enumerate(search_results):
            class_name = result.get_attribute("class")

            if "kno-kp mnr-c g-blk" not in class_name:
                result.screenshot(f'{self.save_dir}/{self.keyword}x{idx}.png')

    def delete_relation_element(self):
        try:
            remove_target = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
            )

            self.browser.execute_script(
                """
            const removeElement = arguments[0];
            removeElement.parentElement.removeChild(removeElement)
            """,
                remove_target)
        except Exception:
            pass

    def close(self):
        self.browser.quit()


googleScreenshot = GoogleSearchResultScreenshooter("buy domain", "screenshots")
googleScreenshot.start()
googleScreenshot.close()

googleScreenshot = GoogleSearchResultScreenshooter(
    "python book", "screenshots")
googleScreenshot.start()
googleScreenshot.close()

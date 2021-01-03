import math
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from util import make_dir


class ResponsiveTester:

    def __init__(self, urls):
        self.sizes = [480, 960, 1366, 1920]
        self.browser_height = 1027
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.dir = 'responsive_test_result'
        make_dir(f'./{self.dir}')

    def screenshot(self, url):
        self.browser.get(url)

        for size in self.sizes:
            self.browser.set_window_size(size, self.browser_height)
            time.sleep(3)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            total_section = math.ceil(scroll_size / self.browser_height)
            for section in range(total_section):
                self.browser.execute_script(
                    f"window.scrollTo(0, {(section) * self.browser_height})")
                time.sleep(2)
                self.browser.save_screenshot(
                    f"{self.dir}/{size}x{section}.png")

    def start(self):
        for url in self.urls:
            self.screenshot(url)


urls = ['https://nomadcoders.co/']
ResponsiveTester(urls).start()

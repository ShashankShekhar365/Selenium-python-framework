from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Base:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")

        #  WebDriverManager handles driver automatically
        service = Service(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service, options=options)

    def teardown_method(self):
        self.driver.quit()
from base.base import Base
from selenium.webdriver.common.by import By
import time

class TestLogin(Base):

    def test_login(self):
        driver = self.driver

        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(2)

        assert "secure area" in driver.find_element(By.ID, "flash").text
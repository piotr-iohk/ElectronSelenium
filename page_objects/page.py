from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Page:
    def __init__(self, driver):
        self.driver = driver


class Element:

    def __init__(self, driver, strategy, locator):
        self.delay = 0.01
        self.timeout = 15
        self.strategy = strategy
        self.locator = locator
        self.driver = driver
        self.element = ""


    def wait_for_element_present(self):
        time.sleep(self.delay)
        self.element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((self.strategy, self.locator)))

    def click(self):
        self.wait_for_element_present()
        # workaround for some wierd Selenium error
        try:
            self.element.click()
        except:
            self.driver.execute_script("arguments[0].click();", self.element)


    def type(self, string):
        self.wait_for_element_present()
        self.element.send_keys(string)

    def get_text(self):
        self.wait_for_element_present()
        return self.element.text





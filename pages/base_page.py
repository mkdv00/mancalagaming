from email import message
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        # Gets url and driver from tests
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
        # Finds one element by locator
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                        message=f"Can't find element with locator {locator}.")

    def find_elements(self, locator, time=10):
        # Finds multiple elements by locator
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                        message=f"Can't find elements with locator {locator}.")

    def find_clickable_element(self, locator, time=10):
        # Finds clickable element by locator
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), 
                                                        message=f"Can't find and click to element with locator {locator}.")

    def open_url(self):
        # Open browser with url
        return self.driver.get(self.url)

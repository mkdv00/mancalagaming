from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage


class HomePageLocators:
    # Class of all locators in home page
    GAMES_LINK_LOCATOR = (By.CSS_SELECTOR, 'ul[role="navigation"] > li:nth-child(2)')
    CONFIRM_OLDER_LOCATOR = (By.CSS_SELECTOR, '.ReactModalPortal button:nth-child(2)')


class HomePage(BasePage):
    # Interaction with the web interface of the home page
    def click_on_games_link(self):
        games_link = self.find_element(HomePageLocators.GAMES_LINK_LOCATOR)
        games_link.click()
        return games_link

    def confirm_older(self):
        # if there is an alert to confirm the age otherwise nothing can be done
        confirm_button = None
        try:
            confirm_button = self.find_clickable_element(HomePageLocators.CONFIRM_OLDER_LOCATOR, time=3)
            confirm_button.click()
        except TimeoutException:
            pass
        return confirm_button

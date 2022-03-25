from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage


class GamesPageLocators:
    # Class of all locators in games page
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    CONFIRM_OLDER_LOCATOR = (By.CSS_SELECTOR, '.ReactModalPortal button:nth-child(2)')
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'footer button')
    GAME_IN_LIST_LOCATOR = (By.CSS_SELECTOR, 'a > div > button')
    GAME_IFRAME_LOCATOR = (By.CSS_SELECTOR, "iframe[allowfullscreen]")


class GamesPage(BasePage):
    # Interaction with the web interface of the games page
    
    def enter_to_search_input(self, game_name):
        # Enter game name in search input
        search_input = self.find_element(GamesPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(game_name)
        return search_input

    def enter_button(self):
        # Click to Return button in search input
        search_input = self.find_element(GamesPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(Keys.RETURN)
        return search_input

    def scroll_to_search_input(self):
        search_input = self.find_element(GamesPageLocators.SEARCH_INPUT)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_input).perform()
        return actions

    def confirm_older(self):
        # if there is an alert to confirm the age otherwise nothing can be done
        confirm_button = None
        try:
            confirm_button = self.find_clickable_element(GamesPageLocators.CONFIRM_OLDER_LOCATOR, time=2)
            confirm_button.click()
        except TimeoutException:
            pass
        return confirm_button

    def accept_cookies(self):
        accept_cookies_button = None
        try:
            accept_cookies_button = self.find_clickable_element(GamesPageLocators.ACCEPT_COOKIES_BUTTON, time=2)
            accept_cookies_button.click()
        except TimeoutException:
            pass
        return accept_cookies_button

    def click_on_game(self):
        game_button = self.find_element(GamesPageLocators.GAME_IN_LIST_LOCATOR)
        game_button.click()
        return game_button

    def get_game_iframe(self):
        game_iframe = self.find_element(GamesPageLocators.GAME_IFRAME_LOCATOR)
        return game_iframe

    def find_game(self, game_name):
        game = None
        try:
            game = self.find_element(GamesPageLocators.GAME_IN_LIST_LOCATOR, time=2)
        except TimeoutException:
            assert False, f"Game with name {game_name} not found."
        return game

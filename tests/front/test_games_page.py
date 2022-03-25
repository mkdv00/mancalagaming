import pytest
import time

from pages.games_page import GamesPage


class TestGamesPage:
    games = ["braindead", "Fruit Factory", "crystal mine"]


    @pytest.mark.games
    @pytest.mark.parametrize("game", games)
    def test_search_games(self, browser, url, game):
        games_page = GamesPage(driver=browser, url=url, route="games")

        games_page.open_url()
        games_page.confirm_older()
        games_page.accept_cookies()
        games_page.enter_to_search_input(game)
        games_page.enter_button()
        games_page.find_game(game)
    
    @pytest.mark.games
    def test_opening_found_games(self, browser, url):
        games_page = GamesPage(driver=browser, url=url, route="games")
        games = ["braindead", "Fruit Factory", "crystal mine"]
        
        game_iframes = []
        for i in range(len(games)):
            games_page.open_url()
            games_page.confirm_older()
            games_page.accept_cookies()
            games_page.enter_to_search_input(games[i])
            games_page.enter_button()
            time.sleep(5)
            games_page.click_on_game()
            game_iframes.append(games_page.get_game_iframe().get_attribute('src'))
        print(f"Games iframes: {game_iframes}")


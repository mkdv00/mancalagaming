import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    # Options for running tests
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox or opera")
    parser.addoption('--host', action='store', default="mancalagaming.org",
                     help="Type host name or the url's instance")


@pytest.fixture(scope='session')
def url(request):
    # Returns the url from the received host
    host: str = request.config.getoption("host")
    new_url: str = f"https://{host}"
    return new_url


@pytest.fixture(scope='session')
def browser(request):
    # Setup and teardown browsers
    browser_name: str = request.config.getoption("browser")
    browser = None

    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        raise pytest.UsageError("--browser should be 'chrome', 'firefox' or 'opera'")

    browser.maximize_window()
    yield browser
    browser.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", 'firefox'], scope='class')
def browser(request):
    """
    the fixture downloads the latest driver and creates the browser instance with passed options
    :param request:
    :return browser instance:
    """
    headless = True
    match request.param:
        case "chrome":
            options = webdriver.ChromeOptions()
            options.headless = headless
            browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)
        case "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = headless
            browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)
    request.cls.driver = browser
    browser.maximize_window()
    yield browser
    browser.quit()

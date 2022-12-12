import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui_tests.pages.data import FormData


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    """
    the fixture downloads the latest driver and creates the browser instance with passed options
    """
    match request.param:
        case "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-dev-shm-usage")
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        case "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-dev-shm-usage")
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()


# set up a hook to be able to check if a test has failed
    def screenshot(self, item):
        allure.attach(self.browser.get_screenshot_as_png(), name=f"Screenshot fail_{item.name}",
                  attachment_type=AttachmentType.PNG)

    @staticmethod
    def pytest_runtest_teardown(item):
        MainPage.screenshot(item)



@pytest.fixture()
def positive_data_case() -> list[tuple[tuple, list]]:
    """
    The fixture returns list of tuples with locators and data passed into fields
    """
    return list(zip(FormData.LOCATORS, FormData.POSITIVE_CASE))


@pytest.fixture(params=FormData.NEGATIVE_CASES)
def negative_data_case(request) -> list[tuple[tuple, list]]:
    """
    The fixture calls one time for each parameter and return values one by one
    """
    return list(zip(FormData.LOCATORS, request.param))

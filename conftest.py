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
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    browser.set_window_size(1920, 1080)
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        screenshot(browser, test_name)
    browser.quit()


def screenshot(browser, name: str):
    allure.attach(browser.get_screenshot_as_png(), name=f"Screenshot {name}", attachment_type=AttachmentType.PNG)


@pytest.fixture
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

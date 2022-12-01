import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    browser.implicitly_wait(0.5)
    yield browser
    browser.quit()

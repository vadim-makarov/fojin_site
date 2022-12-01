from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: By, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_active(self, how: By, what):
        return self.browser.find_element(how, what).is_enabled()

    def go_to_some_page(self, locator: tuple):
        element = self.browser.find_element(*locator)
        element.click()

    def should_be_some_page(self, page_name: str):
        assert page_name in self.browser.current_url, self.browser.current_url

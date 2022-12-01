from time import sleep

import pytest
import requests

from ui_test.pages.locators import Locators
from ui_test.pages.main_page import MainPage


class TestMainPage:
    url = 'https://fojin.tech'

    links_list: list[tuple[str, str]] = [
        Locators.MAIN_PAGE,
        Locators.ABOUT_US,
        Locators.SERVICES,
        Locators.STACK,
        Locators.CASES,
        Locators.CONTACTS
    ]

    endpoints = ['', 'about-us', 'services', 'stack', 'cases', 'contacts']

    def test_main_page_response(self):
        r = requests.get(self.url)
        assert r.status_code == 200, f'Server returned {r.status_code} status code'

    @pytest.mark.parametrize('endpoint, locator', list(zip(endpoints, links_list)))
    def test_link_names(self, browser, endpoint: str, locator: tuple):
        page = MainPage(browser, self.url)
        page.open()
        page.go_to_some_page(locator)
        sleep(1)
        page.should_be_some_page(endpoint)

    # def test_last_instance(self, browser):
    #     page = MainPage(browser, self.url)
    #     page.open()
    #     page.is_element_present(*Locators.CONTACTS)
    #     page.go_to_some_page(Locators.CONTACTS)
    # test_page = MainPage(browser, browser.current_url)
    # page.should_be_some_page('contacts')

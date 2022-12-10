import allure
import pytest
import requests

from ui_tests.pages.locators import MainPageLocators
from ui_tests.pages.main_page import MainPage


class TestMainPage:
    url = f'https://fojin.tech/ru'

    links_list: list[tuple[str, str]] = [
        MainPageLocators.MAIN_PAGE,
        MainPageLocators.ABOUT_US,
        MainPageLocators.SERVICES,
        MainPageLocators.STACK,
        MainPageLocators.CASES,
        MainPageLocators.CONTACTS
    ]

    endpoints = ['', 'about-us', '', '', 'cases', 'contacts']

    bottom_elem_list: list[tuple[str, str]] = [
        MainPageLocators.POLICY,
        MainPageLocators.VK,
        MainPageLocators.TELEGRAM
    ]

    bottom_endpoints = ['policy', 'vk.com/fojin', 't.me/fojin_tech']

    @allure.feature('User can see the main page')
    def test_main_page_response(self):
        """
        server is alive
        """
        r = requests.get(self.url)
        assert r.status_code == 200, f'Server returned {r.status_code} status code'

    @allure.feature('User can go to all top links')
    @pytest.mark.parametrize('endpoint, locator', list(zip(endpoints, links_list)))
    def test_link_names(self, browser, endpoint: str, locator: tuple):
        """
        user can go to all top links from the main page
        """
        page = MainPage(browser, self.url)
        page.open()
        page.scroll_to_and_click_element(locator)
        page.expl_wait_for_page_download(endpoint)
        page.should_be_some_page(endpoint)

    @allure.feature('User can go to the policy page and to the social page links')
    @pytest.mark.parametrize('element, locator', list(zip(bottom_endpoints, bottom_elem_list)))
    def test_bottom_elements_are_active(self, element: str, locator: tuple, browser):
        """
        user can go to all bottom links from the main page
        """
        page = MainPage(browser, self.url)
        page.open()
        page.scroll_to_the_bottom()
        if page.is_element_present(MainPageLocators.COOKIES):
            page.scroll_to_and_click_element(MainPageLocators.COOKIES)  # firefox issue
        page.scroll_to_and_click_element(locator)
        if element != 'policy':
            page.next_window()
        page.expl_wait_for_page_download(element)
        page.should_be_some_page(element)

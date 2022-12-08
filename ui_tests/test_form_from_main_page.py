import os
from time import sleep

import allure
import pytest

from ui_tests.pages.locators import FormLocators
from ui_tests.pages.main_page import MainPage
from ui_tests.pages.data import FormData

username = os.environ.get('USERNAME') or 'username'
password = os.environ.get('PASSWORD') or 'password'


@pytest.fixture()
def positive_data_case() -> list[tuple[tuple,list]]:
    return list(zip(TestMainPageForm.locators, FormData.POSITIVE_CASE))

@pytest.fixture()
def negative_data_case() -> list[tuple[tuple,list]]:
    return list(zip(TestMainPageForm.locators, FormData.EMPTY_CASE))

class TestMainPageForm:
    url = f'https://{username}:{password}@dev.fojin.tech/ru'

    locators = [FormLocators.NAME,
                FormLocators.EMAIL,
                FormLocators.NUMBER,
                FormLocators.ABOUT_PROJECT]

    @allure.feature('User inputs right credentials')
    @allure.description('User is scrolling to the bottom and filling the form')
    def test_positive_form_data(self, browser, positive_data_case: tuple):
        """
          Test fills the application with correct data and checks the popup answer
        """
        page = MainPage(browser, self.url)
        page.open()
        for data in positive_data_case:
            page.input_data_to_form(data)
        page.scroll_to_and_click_element(FormLocators.SEND_BUTTON)
        page.expl_wait_for_elem_visibility(FormLocators.POPUP)
        page.check_popup_is_presented(FormLocators.POPUP)

    @allure.feature("User sends incorrect data")
    @allure.description('User is scrolling to the bottom and trying to send wrong data')
    def test_negative_form_data(self, browser, negative_data_case: tuple):
        """
          Test fills the application with incorrect data and checks the answer
        """
        page = MainPage(browser, self.url)
        page.open()
        for data in negative_data_case:
            page.input_data_to_form(data)
        page.scroll_to_and_click_element(FormLocators.SEND_BUTTON)
        page.check_popup_is_not_presented(FormLocators.POPUP)
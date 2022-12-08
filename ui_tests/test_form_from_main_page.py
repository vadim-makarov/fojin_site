import os
from itertools import zip_longest

import allure
import pytest

from ui_tests.pages.data import FormData
from ui_tests.pages.locators import FormLocators
from ui_tests.pages.main_page import MainPage

username = os.environ.get('USERNAME') or 'username'
password = os.environ.get('PASSWORD') or 'password'


@pytest.fixture()
def positive_data_case() -> list[tuple[tuple, list]]:
    return list(zip(TestMainPageForm.locators, FormData.POSITIVE_CASE))


class TestMainPageForm:
    url = f'https://{username}:{password}@dev.fojin.tech/ru'

    locators: list[tuple[str, str]] = [
        FormLocators.NAME,
        FormLocators.EMAIL,
        FormLocators.NUMBER,
        FormLocators.ABOUT_PROJECT
    ]
    negative_cases = [
        FormData.NEGATIVE_CASE_1,
        FormData.NEGATIVE_CASE_2,
        FormData.NEGATIVE_CASE_3,
        FormData.NEGATIVE_CASE_4
    ]

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
    @pytest.mark.parametrize('case', negative_cases)
    def test_negative_form_data(self, browser, case: list):
        """
          Test fills the application with incorrect data and checks the answer
        """
        page = MainPage(browser, self.url)
        page.open()
        for data in case:
            page.input_data_to_form(data)
        page.scroll_to_and_click_element(FormLocators.SEND_BUTTON)
        page.check_popup_is_not_presented(FormLocators.POPUP)

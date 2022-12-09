import os

import allure
import pytest

from ui_tests.pages.cases_page import CasesPage
from ui_tests.pages.locators import CasesLocators

username = os.environ.get('USERNAME') or 'test_user'
password = os.environ.get('PASSWORD') or 'hellofojin'


class TestCasesPage:
    url = f'https://{username}:{password}@dev.fojin.tech/ru/cases/'

    cases_list = [i for i in '123456789']

    locators: list[tuple[str, str]] = [
        CasesLocators.CASE_1,
        CasesLocators.CASE_2,
        CasesLocators.CASE_3,
        CasesLocators.CASE_4,
        CasesLocators.CASE_5,
        CasesLocators.CASE_6,
        CasesLocators.CASE_7,
        CasesLocators.CASE_8,
        CasesLocators.CASE_9,
    ]

    @allure.feature('User can see all the cases')
    @pytest.mark.parametrize('case, locator', list(zip(cases_list, locators)))
    def test_case_page(self, browser, case: str, locator: tuple):
        """
        test checks availability of each case page(doesn't check content!)
        """
        page = CasesPage(browser, self.url)
        page.open()
        page.expl_wait_for_page_download('cases')
        page.scroll_to_and_click_element(locator)
        page.expl_wait_for_page_download(case)
        page.should_be_some_page(case)
        page.screenshot(case)

import allure
import pytest

from ui_tests.pages.cases_page import CasesPage
from ui_tests.pages.data import CasesData


@pytest.mark.xfail(reason="the test fails in a window mode")
class TestCasesPage:
    url = f'https://fojin.tech/ru/cases/'

    @allure.feature('User can see all the cases')
    @pytest.mark.parametrize('case, locator', list(zip(CasesData.cases_list, CasesData.locators)))
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

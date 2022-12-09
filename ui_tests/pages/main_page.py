import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.data import FormData
from ui_tests.pages.locators import FormLocators


class MainPage:
    def __init__(self, browser, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_element_active(self, locator: tuple):
        return self.browser.find_element(*locator).is_enabled()

    def scroll_to_and_click_element(self, locator: tuple):
        element = self.browser.find_element(*locator)
        element.location_once_scrolled_into_view
        if locator:
            if 'case-container-5' in locator[1]:
                self.browser.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_UP)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(element))
        element.click()

    def should_be_some_page(self, page_name: str):
        assert page_name in self.browser.current_url, self.browser.current_url

    def scroll_to_the_bottom(self):
        html = self.browser.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)

    def expl_wait_for_page_download(self, element: str):
        try:
            WebDriverWait(self.browser, 5).until(EC.url_matches(element))
        except TimeoutException:
            return False
        return True

    def expl_wait_for_elem_visibility(self, locator: tuple):
        try:
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def next_window(self):
        """
        changes the active window
        """
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def input_data_to_form(self, data: tuple):
        """
        Receives locator and data. Finds a form and passes the data into it
        """
        self.browser.find_element(*data[0]).send_keys(data[1])

    def check_popup_is_presented(self, locator):
        """
        Test checks that success message appears
        """
        popup = self.browser.find_element(*locator)
        print(popup.text)
        assert popup.is_displayed(), 'Not success popup presented'
        assert FormData.SUCCESS_TEXT in popup.text, "No success text presented"

    def check_popup_is_not_presented(self, locator):
        """
        Test checks that
        error message appears and success message doesn't
        when the user sends wrong data into all the fields
        """
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            assert not self.is_element_present(locator), 'It seems that success message appeared'
            assert FormData.UNSUCCESSFUL_TEXT in FormLocators.FORM, 'There is no unsuccessful message in the form'

    def screenshot(self, name: str):
        allure.attach(self.browser.get_screenshot_as_png(), name=f"Screenshot {name}",
                      attachment_type=AttachmentType.PNG)

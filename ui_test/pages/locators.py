from selenium.webdriver.common.by import By


class Locators:
    MAIN_PAGE = (By.CSS_SELECTOR, '.sc-34a158a0-1 > a:nth-child(1) > img:nth-child(1)')
    ABOUT_US = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(1)')
    SERVICES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(2)')
    STACK = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(3)')
    CASES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(4)')
    CONTACTS = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(5)')

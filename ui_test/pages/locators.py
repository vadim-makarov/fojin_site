from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.CSS_SELECTOR, '.sc-34a158a0-1 > a:nth-child(1) > img:nth-child(1)')
    ABOUT_US = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(1)')
    SERVICES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(2)')
    STACK = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(3)')
    CASES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(4)')
    CONTACTS = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(5)')
    POLICY = (
        By.CSS_SELECTOR, '#form > div > div > form > div:nth-child(2) > div.sc-63050886-2.gpFpVi > span > span > a')
    VK = (By.CSS_SELECTOR, '#__next > footer > div > div > div.sc-5e48d489-2.dapqUa > a.sc-5e48d489-4.cWBrfq')
    TELEGRAM = (By.CSS_SELECTOR, '#__next > footer > div > div > div.sc-5e48d489-2.dapqUa > a.sc-5e48d489-4.bZukxn')
    COOKIES = (By.CSS_SELECTOR, '#cookieConsent > div > button')
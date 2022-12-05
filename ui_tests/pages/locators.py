from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.CSS_SELECTOR, '.sc-fbcb99c0-1 > a:nth-child(1) > img:nth-child(1)')
    ABOUT_US = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(1)')
    SERVICES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(2)')
    STACK = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(3)')
    CASES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(4)')
    CONTACTS = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(5)')
    POLICY = (By.CSS_SELECTOR, '.sc-63050886-5')
    VK = (By.CSS_SELECTOR, 'a.sc-5e48d489-4:nth-child(1)')
    TELEGRAM = (By.CSS_SELECTOR, 'a.sc-5e48d489-4:nth-child(2)')
    COOKIES = (By.CSS_SELECTOR, '.sc-2a084499-3')


class CasesLocators:
    CASE_1 = (By.CSS_SELECTOR, '.case-container-1 > div:nth-child(2) > div:nth-child(1)')  # EdTech
    CASE_2 = (By.CSS_SELECTOR, '.case-container-2 > div:nth-child(1) > div:nth-child(1)')  # E-commerce
    CASE_3 = (By.CSS_SELECTOR, '.case-container-3 > div:nth-child(1) > div:nth-child(1)')  # Entertainment, marketing
    CASE_4 = (By.CSS_SELECTOR, '.case-container-4 > div:nth-child(2) > div:nth-child(1)')  # Business, B2B
    CASE_5 = (By.CSS_SELECTOR, '.case-container-5 > div:nth-child(2) > div:nth-child(1)')  # Crypto !!!Flaky!!!
    CASE_6 = (By.CSS_SELECTOR, '.case-container-6 > div:nth-child(1) > div:nth-child(1)')
    CASE_7 = (By.CSS_SELECTOR, '.case-container-7 > div:nth-child(1) > div:nth-child(1)')
    CASE_8 = (By.CSS_SELECTOR, '.case-container-8 > div:nth-child(1) > div:nth-child(1)')
    CASE_9 = (By.CSS_SELECTOR, '.case-container-9 > div:nth-child(1) > div:nth-child(1)')

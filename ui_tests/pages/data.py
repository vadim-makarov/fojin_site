from ui_tests.pages.locators import FormLocators


class FormData:
    POSITIVE_CASE = ['test_user', 'test@fojin.tech', '12345678901', 'some useless information']
    SUCCESS_TEXT = 'Сообщение отправлено. В ближайшее время мы с вами свяжемся'
    UNSUCCESSFUL_TEXT = 'Поле обязательно'
    LOCATORS: list[tuple[str, str]] = [
        FormLocators.NAME,
        FormLocators.EMAIL,
        FormLocators.NUMBER,
        FormLocators.ABOUT_PROJECT
    ]
    NEGATIVE_CASE_1 = ['          ', 'test@fojin.tech', '12345678901', 'some useless information']
    NEGATIVE_CASE_2 = ['test_user', '', '12345678901', 'some useless information']
    NEGATIVE_CASE_3 = ['test_user', 'test@fojin.tech', '   ', 'some useless information']
    NEGATIVE_CASE_4 = ['test_user', 'test@fojin.tech', '12345678901', '     ']
    NEGATIVE_CASES = [NEGATIVE_CASE_1, NEGATIVE_CASE_2, NEGATIVE_CASE_3, NEGATIVE_CASE_4]

from ui_tests.pages.locators import FormLocators


class FormData:
    POSITIVE_CASE = ['test_user', 'test@fojin.tech', '12345678901', 'some useless information']
    SUCCESS_TEXT = 'Сообщение отправлено. В ближайшее время мы с вами свяжемся'
    UNSUCCESSFUL_TEXT = 'Поле обязательно'
    NEGATIVE_CASE_1 = zip(['          ',
        'test@fojin.tech',
        '12345678901',
        'some useless information'
    ],
        [
            FormLocators.NAME,
            FormLocators.EMAIL,
            FormLocators.NUMBER,
            FormLocators.ABOUT_PROJECT
        ])
    NEGATIVE_CASE_2 = zip(['test_user', '', '12345678901', 'some useless information'],
        [
            FormLocators.NAME,
            FormLocators.EMAIL,
            FormLocators.NUMBER,
            FormLocators.ABOUT_PROJECT
        ])
    NEGATIVE_CASE_3 = zip(['test_user', 'test@fojin.tech', '   ', 'some useless information'],
                               [
                                   FormLocators.NAME,
                                   FormLocators.EMAIL,
                                   FormLocators.NUMBER,
                                   FormLocators.ABOUT_PROJECT
                               ])
    NEGATIVE_CASE_4 = zip(['test_user', 'test@fojin.tech', '12345678901', '     '],
                               [
                                   FormLocators.NAME,
                                   FormLocators.EMAIL,
                                   FormLocators.NUMBER,
                                   FormLocators.ABOUT_PROJECT
                               ])

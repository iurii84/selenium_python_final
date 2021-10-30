from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        page_url = self.browser.current_url
        assert page_url == LoginPageLocators.LOGIN_URL,  f"login page's URL is not as expected '{page_url}' received " \
                                                         f"and {LoginPageLocators.LOGIN_URL} expected "

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"Login form is not presented! Check if " \
                                                                       f"{LoginPageLocators.LOGIN_FORM} locator is " \
                                                                       f"correct "

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), f"Register form is not presented! Check if " \
                                                                          f"{LoginPageLocators.REGISTER_FORM} locator" \
                                                                          f" is correct"

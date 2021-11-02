import time
from random import randrange

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
        assert page_url == LoginPageLocators.LOGIN_URL, f"login page's URL is not as expected '{page_url}' received " \
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

    def register_new_user(self):
        email_field_el = self.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field_el.send_keys(generate_email())

        password = generate_pass()

        password_field_el = self.find_element(*LoginPageLocators.REGISTER_PASS_FIELD)
        password_field_el.send_keys(password)

        password_confirmation_field_el = self.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRMATION_FIELD)
        password_confirmation_field_el.send_keys(password)

        register_button_el = self.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button_el.click()


def generate_email():
    return str(time.time()) + "@fakemail.org"


def generate_pass():
    return str(randrange(10000, 99000)) + "argsd"

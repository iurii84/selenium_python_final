from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/_fake"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_fake")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_fake")

# TODO - DELETE '_fake'

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_ITEM_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner :nth-child(1) > strong")

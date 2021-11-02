from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS_CONFIRMATION_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_ITEM_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner :nth-child(1) > strong")

    EXPECTED_ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    EXPECTED_ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_URL = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators:
    ITEMS_IN_CART = (By.CSS_SELECTOR, "basket-items")
    NO_ITEMS_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

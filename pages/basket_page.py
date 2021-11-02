from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):
    def wait_for_not_have_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS_IN_CART), \
            "Items are presented in cart, but should not be"

    def wait_for_text_that_cart_is_empty(self):
        assert self.is_element_present(*CartPageLocators.NO_ITEMS_IN_CART_MESSAGE), \
            "Not found the confirmation message, that the cart is empty"


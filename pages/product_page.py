import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        self.is_item_in_cart()
        self.is_cart_price_the_same_as_added_item_price()

    def is_item_in_cart(self):
        add_to_cart_btn = self.wait_for_item_and_get_it(*ProductPageLocators.ADD_ITEM_TO_CART_BTN, 5)
        add_to_cart_btn.click()

        self.solve_quiz_and_get_code()

        added_item_el = self.wait_for_item_and_get_it(*ProductPageLocators.ADDED_ITEM, 5)
        added_item_text = added_item_el.text
        expected_item_text = "The shellcoder's handbook"
        assert added_item_text == expected_item_text, f"wrong item's text added! " \
                                                      f"Expected '{expected_item_text}'," \
                                                      f" but got '{added_item_text}'"

    def is_cart_price_the_same_as_added_item_price(self):
        cart_total_price_el = self.find_element(*ProductPageLocators.CART_TOTAL_PRICE)
        total_price_no_format_txt = cart_total_price_el.text
        total_price = find_float_in_str(total_price_no_format_txt)
        expected_price = 9.99
        assert total_price == expected_price, f"wrong price! " \
                                              f"Expected '{expected_price}'," \
                                              f" but got '{total_price}'"


def find_float_in_str(string):
    str_res = ''
    for ch in string:
        if ch.isdigit() or ch == "." or ch == ",":
            if ch == ",":
                str_res += "."
            else:
                str_res += ch
    return float(str_res)

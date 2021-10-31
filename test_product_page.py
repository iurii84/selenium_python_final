import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_cart()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.is_disappeared_from_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# pytest -s --language=ru test_product_page.py

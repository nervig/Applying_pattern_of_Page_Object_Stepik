import time

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()
#
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_note_basket_is_empty()
    # time.sleep(10)


# def test_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#     page.should_be_login_form()
#     page.should_be_register_form()
# browser.get(link)
# login_link = browser.find_element_by_css_selector("#login_link")
# login_link.click()

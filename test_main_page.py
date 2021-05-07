from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

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

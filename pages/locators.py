from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CLASS_NAME, "btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_ID = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    GOODS_ON_PAGE = (By.TAG_NAME, "h1")
    STRONG_TAG = (By.TAG_NAME, "#messages .alertinner strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
    GOODS_COST_CLASS = (By.TAG_NAME, "div.product_main > p")
    GOODS_COST = (By.TAG_NAME, "div.hidden-xs")

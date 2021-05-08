import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, "Page is not exist"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ID).send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD_1).send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD_2).send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()

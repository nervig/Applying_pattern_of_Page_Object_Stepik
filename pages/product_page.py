from .base_page import BasePage
from .locators import ProductPageLocators
import re


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_basket_button()
        self.solve_quiz_and_get_code()

    def should_be_basket_button(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        product_link.click()

    def should_be_good_in_basket(self):
        h1_tag = self.browser.find_element(*ProductPageLocators.GOODS_ON_PAGE)
        h1_text = h1_tag.text
        strong_tag = self.browser.find_element(*ProductPageLocators.STRONG_TAG)
        strong_text = strong_tag.text
        link = self.browser.current_url
        assert h1_text == strong_text, f"The goods in basket doesn't equal selected{link}"

    def should_be_equals_cost(self):
        pattern = r'\d+.\d+'
        goods_cost_class = self.browser.find_element(*ProductPageLocators.GOODS_COST_CLASS)
        goods_cost = re.search(pattern, goods_cost_class.text)
        cost_class = self.browser.find_element(*ProductPageLocators.GOODS_COST)
        cost_in_basket = re.search(pattern, cost_class.text)
        assert goods_cost[0] == cost_in_basket[0], "The price of goods on page doesn't equal the price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_element_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "element exists"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Element is present"


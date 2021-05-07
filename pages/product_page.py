from .base_page import BasePage
from .locators import ProductPageLocators
import re


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_basket_button()
        self.solve_quiz_and_get_code()

    def should_be_basket_button(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)  # to locators
        # file should add the PRODUCT_LINK
        product_link.click()

    def should_be_good_in_basket(self):
        h1_tag = self.browser.find_element_by_tag_name("h1")
        h1_text = h1_tag.text
        strong_tag = self.browser.find_element_by_tag_name("div.alertinner > strong")
        strong_text = strong_tag.text
        assert h1_text == strong_text, "The goods in basket doesn't equal selected"

    def should_be_equals_cost(self):
        pattern = r'\d.\d+'
        goods_cost_class = self.browser.find_element_by_tag_name("div.product_main > p")
        goods_cost = re.search(pattern, goods_cost_class.text)
        cost_class = self.browser.find_element_by_tag_name("div.hidden-xs")
        cost_in_basket = re.search(pattern, cost_class.text)
        assert goods_cost[0] == cost_in_basket[0], "The price of goods on page doesn't equal the price in basket"
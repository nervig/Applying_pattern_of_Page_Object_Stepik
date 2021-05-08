from .base_page import BasePage
import re


class BasketPage(BasePage):
    def should_be_note_basket_is_empty(self):
        pattern = r'^[A-Za-z ]+'
        note_id = self.browser.find_element_by_tag_name("#content_inner")
        note_basket_is_empty = re.search(pattern, note_id.text)
        # print(note_basket_is_empty[0])
        assert note_basket_is_empty[0] == "Your basket is empty", "Note 'Your basket is empty' not exists"
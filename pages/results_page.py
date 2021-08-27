from selenium.webdriver.common.by import By

from pages.base_page import Page

class ResultsPage(Page):
    SEARCH_SELECT_RESULT = (By.CSS_SELECTOR, '.s-desktop-toolbar .a-color-base')

    def verify_department_header_result(self, expected_text: str):
        self.verify_element_text(expected_text, *self.SEARCH_SELECT_RESULT)
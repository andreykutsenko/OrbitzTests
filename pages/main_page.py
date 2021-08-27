from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'location-field-leg1-origin')
    SEARCH_INPUT_DEST = (By.ID, 'location-field-leg1-destination')
    SEARCH_BUTTON = (By.ID, 'headerSearchButton')
    SELECT_CITY = (By.XPATH, "//ul[@class='uitk-typeahead-results no-bullet']/li")

    def open(self):
        self.open_page('https://www.orbitz.com/')

    def input_city(self, city_field: str, city_text: str):
        self.click(By.XPATH, f"//button[@aria-label='{city_field}']")
        if 'to' in city_field:
            self.input(city_text, *self.SEARCH_INPUT_DEST)
        else:
            self.input(city_text, *self.SEARCH_INPUT)
        self.click_at_first_in_list(*self.SELECT_CITY)
        sleep(3)
    # def verify_dropdown(self):
    #     self.wait_for_element_appear(*self.DROPDOWN_MENU_LOCATOR)
    #     self.click(*self.DROPDOWN_MENU_LOCATOR)
    def click_tab(self, tab_text: str):
        self.click(By.XPATH, f"//span[@class='uitk-tab-text' and text()='{tab_text}']")
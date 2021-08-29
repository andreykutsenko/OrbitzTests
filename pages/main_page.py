from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):
    SEARCH_FLYING_FROM = (By.ID, 'location-field-leg1-origin')
    SEARCH_FLYING_TO = (By.ID, 'location-field-leg1-destination')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-testid=submit-button]')
    SELECT_BUTTON = (By.XPATH, "//button[@data-test-id='select-button']")
    DONE_BUTTON = (By.CSS_SELECTOR, '[data-stid=apply-date-picker]')
    SELECT_CITY_FROM = (By.XPATH, "//*[@id='location-field-leg1-origin-menu']//li[@class='uitk-typeahead-result-item has-subtext']")
    SELECT_CITY_TO = (By.XPATH, "//*[@id='location-field-leg1-destination-menu']//li[@class='uitk-typeahead-result-item has-subtext']")
    LOCATOR_DEPARTING = (By.ID, 'd1-btn')
    LOCATOR_RETURNING = (By.ID, 'd2-btn')
    # NONSTOP_BUTTON = (By.ID, 'stops-0')
    NONSTOP_BUTTON = (By.CSS_SELECTOR, ".uitk-switch.uitk-checkbox #stops-0")
    SELECT_OPTIONS_LOCATOR = (By.ID, 'listings-sort')
    LOCATOR_MAX_EXP = (By.XPATH, "//ul[@data-test-id='listings']/li")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test-id='goto-checkout-button']")

    def open(self):
        self.open_page('https://www.orbitz.com/')

    def input_city(self, city_field: str, city_text: str):
        self.click(By.XPATH, f"//button[@aria-label='{city_field}']")
        if 'to' in city_field:
            self.input(city_text, *self.SEARCH_FLYING_TO)
            self.click_at_first_in_list(*self.SELECT_CITY_TO)
        else:
            self.input(city_text, *self.SEARCH_FLYING_FROM)
            self.click_at_first_in_list(*self.SELECT_CITY_FROM)

    def click_tab(self, tab_text: str):
        if 'Nonstop' in tab_text:
            self.wait_for_element_appear(*self.NONSTOP_BUTTON)
            self.click(*self.NONSTOP_BUTTON)
        else:
            self.click(By.XPATH, f"//span[@class='uitk-tab-text' and text()='{tab_text}']")

    def input_date(self, start_trip_week: str, back_trip_week: str):
        dict_details = self.flight_details(start_trip_week, back_trip_week)
        start_date = dict_details["start_date"]
        back_date = dict_details["back_date"]
        start_month = dict_details["start_month"]
        back_month = dict_details["back_month"]

        self.click(*self.LOCATOR_DEPARTING)
        start_locator = f"//div[@class='uitk-date-picker-menu-months-container']//tbody//button[@data-day='{start_date}' and contains(@aria-label,'{start_month}')]"
        self.click(By.XPATH, start_locator)
        self.click(*self.DONE_BUTTON)
        self.click(*self.LOCATOR_RETURNING)
        back_locator = f"//div[@class='uitk-date-picker-menu-months-container']//tbody//button[@data-day='{back_date}' and contains(@aria-label,'{back_month}')]"
        self.click(By.XPATH, back_locator)
        self.click(*self.DONE_BUTTON)

    def click_icon(self):
        self.click(*self.SEARCH_BUTTON)

    def select_search_option(self, option):
        self.select_options(option, *self.SELECT_OPTIONS_LOCATOR)

    def select_max_exp(self, option):
        self.click_at_first_in_list(*self.LOCATOR_MAX_EXP)
        self.click(*self.SELECT_BUTTON)
        sleep(3)
        try:
            self.click_tab('Nonstop')
        finally:
            self.select_options(option, *self.SELECT_OPTIONS_LOCATOR)
        self.click_at_first_in_list(*self.LOCATOR_MAX_EXP)
        self.click(*self.SELECT_BUTTON)

        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)


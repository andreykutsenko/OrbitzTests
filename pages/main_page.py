from selenium.webdriver.common.by import By
from pages.base_page import Page

from datetime import date
from dateutil.relativedelta import relativedelta


class MainPage(Page):
    SEARCH_FLYING_FROM = (By.ID, 'location-field-leg1-origin')
    SEARCH_FLYING_TO = (By.ID, 'location-field-leg1-destination')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-testid=submit-button]')
    DONE_BUTTON = (By.CSS_SELECTOR, '[data-stid=apply-date-picker]')
    SELECT_CITY_FROM = (By.XPATH, "//*[@id='location-field-leg1-origin-menu']//li[@class='uitk-typeahead-result-item has-subtext']")
    SELECT_CITY_TO = (By.XPATH, "//*[@id='location-field-leg1-destination-menu']//li[@class='uitk-typeahead-result-item has-subtext']")
    LOCATOR_DEPARTING = (By.ID, 'd1-btn')
    LOCATOR_RETURNING = (By.ID, 'd2-btn')

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
        self.click(By.XPATH, f"//span[@class='uitk-tab-text' and text()='{tab_text}']")

    def input_date(self, start_trip_week: str, back_trip_week: str):
        period_start = date.today() + relativedelta(weeks=+int(start_trip_week))
        period_back = date.today() + relativedelta(weeks=+int(back_trip_week))
        start_date = str(int(period_start.strftime('%d')))
        start_month = period_start.strftime('%b')
        back_date = str(int(period_back.strftime('%d')))
        back_month = period_back.strftime('%b')
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
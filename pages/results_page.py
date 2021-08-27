from selenium.webdriver.common.by import By
from pages.base_page import Page

from datetime import date
from dateutil.relativedelta import relativedelta


class ResultsPage(Page):
    FLYING_FROM_TEXT = (By.CSS_SELECTOR, "#typeahead-originInput-0-menu button.uitk-faux-input")
    FLYING_TO_TEXT = (By.CSS_SELECTOR, "#typeahead-destinationInput-0-menu button.uitk-faux-input")
    START_DATE = (By.CSS_SELECTOR, "button#start-date-ROUND_TRIP-0-btn")
    END_DATE = (By.CSS_SELECTOR, "button#end-date-ROUND_TRIP-0-btn")

    def verify_search_result(self, city_from: str, city_to: str, start_trip_week: str, back_trip_week: str):
        period_start = date.today() + relativedelta(weeks=+int(start_trip_week))
        period_back = date.today() + relativedelta(weeks=+int(back_trip_week))
        start_date = str(int(period_start.strftime('%d')))
        start = f"{period_start.strftime('%b')} {start_date}"
        back_date = str(int(period_back.strftime('%d')))
        back = f"{period_back.strftime('%b')} {back_date}"

        self.verify_element_text(city_from, *self.FLYING_FROM_TEXT)
        self.verify_element_text(city_to, *self.FLYING_TO_TEXT)
        self.verify_element_text(start, *self.START_DATE)
        self.verify_element_text(back, *self.END_DATE)
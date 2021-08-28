from selenium.webdriver.common.by import By
from pages.base_page import Page


class ResultsPage(Page):
    FLYING_FROM_TEXT = (By.CSS_SELECTOR, "#typeahead-originInput-0-menu button.uitk-faux-input")
    FLYING_TO_TEXT = (By.CSS_SELECTOR, "#typeahead-destinationInput-0-menu button.uitk-faux-input")
    START_DATE = (By.CSS_SELECTOR, "button#start-date-ROUND_TRIP-0-btn")
    END_DATE = (By.CSS_SELECTOR, "button#end-date-ROUND_TRIP-0-btn")
    FLYING_TRIP_0 = (By.CSS_SELECTOR, "div[data-test-id=flight-review-0] h2.uitk-heading-4")
    FLYING_TRIP_1 = (By.XPATH, "//div[@data-test-id='flight-review-1']/div[@data-test-id='flight-review-header']//h2")
    DATE_TRIP_0 = (By.XPATH, "//div[@data-test-id='flight-review-0']//div[@data-test-id='flight-operated']")
    DATE_TRIP_1 = (By.XPATH, "//div[@data-test-id='flight-review-1']//div[@data-test-id='flight-operated']")

    def verify_search_result(self, city_from: str, city_to: str, start_trip_week: str, back_trip_week: str):
        dict_details = self.flight_details(start_trip_week, back_trip_week)
        start = dict_details["start"]
        back = dict_details["back"]
        self.verify_element_text(city_from, *self.FLYING_FROM_TEXT)
        self.verify_element_text(city_to, *self.FLYING_TO_TEXT)
        self.verify_element_text(start, *self.START_DATE)
        self.verify_element_text(back, *self.END_DATE)

    def verify_flight_result(self, city_from: str, city_to: str, start_trip_week: str, back_trip_week: str):
        dict_details = self.flight_details(start_trip_week, back_trip_week)
        start = dict_details["start"]
        back = dict_details["back"]
        expected_trip_0 = f"{city_from} to {city_to[:city_to.find(',')]}"
        expected_trip_1 = f"{city_to[:city_to.find(',')]} to {city_from}"

        self.wait_for_element_appear(*self.FLYING_TRIP_0)
        self.verify_element_text(expected_trip_0, *self.FLYING_TRIP_0)
        self.verify_element_text(expected_trip_1, *self.FLYING_TRIP_1)
        self.verify_element_text(start, *self.DATE_TRIP_0)
        self.verify_element_text(back, *self.DATE_TRIP_1)
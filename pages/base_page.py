from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import date
from dateutil.relativedelta import relativedelta


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text: str, *locator):
        input_field = self.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def click(self, *locator):
        self.find_element(*locator).click()

    def click_at_first_in_list(self, *locator):
        self.find_elements(*locator)[0].click()

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def select_options(self, option, *locator):
        select = Select(self.find_element(*locator))
        select.select_by_visible_text(option)

    def verify_element_text(self, expected_text: str, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} text, but got {actual_text} text'

    def flight_details(self, start_trip_week: str, back_trip_week: str):
        period_start = date.today() + relativedelta(weeks=+int(start_trip_week))
        period_back = date.today() + relativedelta(weeks=+int(back_trip_week))
        start_date = str(int(period_start.strftime('%d')))
        back_date = str(int(period_back.strftime('%d')))
        start = f"{period_start.strftime('%b')} {start_date}"
        back = f"{period_back.strftime('%b')} {back_date}"
        start_month = period_start.strftime('%b')
        back_month = period_back.strftime('%b')
        return {
            "start": start,
            "back": back,
            "start_month": start_month,
            "back_month": back_month,
            "start_date": start_date,
            "back_date": back_date
        }
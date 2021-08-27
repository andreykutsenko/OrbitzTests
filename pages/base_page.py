from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

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

    def verify_element_text(self, expected_text: str, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} text, but got {actual_text} text'

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()
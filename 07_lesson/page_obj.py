from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.result_display = (By.CSS_SELECTOR, '.screen')

    def open(self):
        url = ("https://bonigarcia.dev/selenium-webdriver-java/"
               "slow-calculator.html")
        self.driver.get(url)

    def set_delay(self, delay):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button(self, button_text):
        button = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button).click()

    def get_result(self):
        return self.driver.find_element(*self.result_display).text

    def wait_for_result(self, expected_result, timeout):
        WebDriverWait(self.driver, timeout + 1).until(
            EC.text_to_be_present_in_element(
                self.result_display, expected_result
            )
        )

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    time.sleep(2)

    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    time.sleep(1)

    updated_button_text = driver.find_element(
        By.CSS_SELECTOR, "#updatingButton"
    ).text
    print(updated_button_text)

    time.sleep(2)

finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    
    # Явное ожидание появления поля ввода
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # Явное ожидание, что кнопка станет кликабельной
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
    )
    button.click()

    # Явное ожидание, что текст кнопки обновится
    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )
    
    # Получаем и выводим текст кнопки
    button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(button_text)

finally:
    driver.quit() 
    
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Запускаем Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Открыть страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Установить задержку 45 секунд
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Нажать кнопку 7
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    
    # Нажать кнопку +
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    
    # Нажать кнопку 8
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    
    # Нажать кнопку =
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    # Ждем, пока результат станет 15 (максимум 50 секунд)
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    
    # Проверяем, что результат равен 15
    assert result, "Результат не равен 15"
    
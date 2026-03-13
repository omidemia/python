import pytest
from selenium import webdriver
from page_obj import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    page = CalculatorPage(driver)

    print("1. Открываем страницу калькулятора...")
    page.open()

    print("2. Вводим задержку 45 секунд...")
    page.set_delay("45")

    print("3. Нажимаем кнопки 7 + 8 =...")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    print("4. Ждем результат 15...")
    page.wait_for_result("15", 45)

    print("5. Проверяем результат...")
    assert page.get_result() == "15"
    print("✅ Тест пройден! Результат 15")

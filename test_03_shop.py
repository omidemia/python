import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    # Запускаем Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    # Шаг 1: Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")
    
    # Шаг 2: Авторизоваться
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Шаг 3: Добавить товары в корзину
    # Ожидаем загрузки страницы с товарами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    
    # Добавляем Sauce Labs Backpack
    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    
    # Добавляем Sauce Labs Bolt T-Shirt
    bolt_tshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    bolt_tshirt.click()
    
    # Добавляем Sauce Labs Onesie
    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie.click()
    
    # Шаг 4: Перейти в корзину
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
    
    # Шаг 5: Нажать Checkout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()
    
    # Шаг 6: Заполнить форму своими данными
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Иван")
    
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Петров")
    
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("123456")
    
    # Шаг 7: Нажать Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    # Шаг 8: Прочитать итоговую стоимость
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total = total_text.replace("Total: ", "")
    
    # Шаг 9: Проверить, что итоговая сумма равна $58.29
    assert total == "$58.29", f"Ожидалось $58.29, получено {total}"
    
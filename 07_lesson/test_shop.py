import pytest
from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    print("1. Открываем сайт...")
    login_page.open()

    print("2. Входим в систему...")
    login_page.login("standard_user", "secret_sauce")

    print("3. Добавляем товары в корзину...")
    main_page.add_to_cart("Sauce Labs Backpack")
    main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_to_cart("Sauce Labs Onesie")

    print("4. Переходим в корзину...")
    main_page.go_to_cart()

    print("5. Нажимаем Checkout...")
    cart_page.click_checkout()

    print("6. Заполняем форму...")
    checkout_page.fill_info("Иван", "Иванов", "123456")

    print("7. Читаем итоговую стоимость...")
    total = checkout_page.get_total()
    print(f"Итоговая стоимость: {total}")

    print("8. Проверяем результат...")
    assert total == "Total: $58.29", \
        f"Ожидалась сумма 'Total: $58.29', получена '{total}'"
    print("✅ Тест пройден! Сумма верная.")

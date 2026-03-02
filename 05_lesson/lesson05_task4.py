from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

# Вводим логин
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Вводим пароль
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login (ищем по типу submit)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(2)

# Выводим текст зелёной плашки
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print("✅ Зелёная плашка:", success_message.text)

sleep(3)
driver.quit()
print("🚪 Браузер закрыт")

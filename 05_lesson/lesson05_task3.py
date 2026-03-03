from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")
sleep(2)

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Sky")
print("✅ Введен текст: Sky")
sleep(1)

input_field.clear()
print("✅ Поле очищено")
sleep(1)

input_field.send_keys("Pro")
print("✅ Введен текст: Pro")
sleep(2)

driver.quit()
print("🚪 Браузер закрыт")

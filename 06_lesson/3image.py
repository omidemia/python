from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

# Ждем загрузки картинок
wait = WebDriverWait(driver, 20)

# Ждем появления картинки с id="award" (это и есть 3-я картинка)
wait.until(
    EC.presence_of_element_located((By.ID, "award"))
)

# Находим картинку по ID
award_image = driver.find_element(By.ID, "award")
src_value = award_image.get_attribute("src")

# Выводим значение в консоль
print(src_value)

# Чтобы увидеть результат, добавляем ожидание
input("Нажмите Enter, чтобы закрыть браузер...")

driver.quit()

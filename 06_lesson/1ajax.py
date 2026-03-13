from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://www.uitestingplayground.com/ajax")

    # Кликаем по синей кнопке
    driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

    # Явно ждем появления зеленой плашки (максимум 20 секунд)
    wait = WebDriverWait(driver, 20)
    green_label = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    # Получаем текст и выводим в консоль
    txt = green_label.text
    print(txt)

finally:
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service


@pytest.fixture
def driver():
    service = Service(r"C:\Users\Александра\Desktop\06K_lesson\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    # Шаг 1: Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Шаг 2: Дождаться загрузки формы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )
    
    # Шаг 3: Заполнить форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    # Шаг 4: Нажать кнопку
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # Шаг 5: Дождаться результатов
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert"))
    )
    
    # Шаг 6: Проверить Zip code (красный)
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")
    
    # Шаг 7: Проверить остальные поля (зеленые)
    fields = ["first-name", "last-name", "address", "e-mail", 
              "phone", "city", "country", "job-position", "company"]
    
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class")
        
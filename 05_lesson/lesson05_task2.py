from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.get("http://uitestingplayground.com/dynamicid")
driver.fullscreen_window()
sleep(2)

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

print("✅ Синяя кнопка нажата!")

sleep(5)

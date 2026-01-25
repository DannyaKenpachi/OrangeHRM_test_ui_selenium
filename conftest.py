import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    # Создаем объект настроек
    options = Options()

    # САМАЯ ВАЖНАЯ ЧАСТЬ
    # Проверяем: "Я сейчас на Линуксе?" (GitHub Actions всегда Linux)
    if sys.platform.startswith("linux"):
        print("\nЗапуск на сервере (Linux) -> Включаем Headless!")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        # Иначе (Windows/Mac) -> Запускаем с окном
        print("\nЗапуск локально -> Включаем GUI")
        options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    # Передаем options обязательно!
    driver = webdriver.Chrome(service=service, options=options)
    # 
    yield driver
    driver.quit()

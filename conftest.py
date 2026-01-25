import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--headless", 
        action="store_true", 
        default=False, 
        help="Запустить браузер в скрытом режиме (без GUI)"
    )

@pytest.fixture()
def driver():
    service_obj = Service(ChromeDriverManager().install())
    driver_obj  = webdriver.Chrome(service=service_obj)

    driver_obj.maximize_window()
    yield driver_obj
    driver_obj.quit()
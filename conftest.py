import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    service_obj = Service(ChromeDriverManager().install())
    driver_obj  = webdriver.Chrome(service=service_obj)

    driver_obj.maximize_window()
    yield driver_obj
    driver_obj.quit()
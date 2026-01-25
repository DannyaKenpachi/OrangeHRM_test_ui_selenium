import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--headless", 
        action="store_true", 
        default=False, 
        help="Запустить браузер в скрытом режиме (без GUI)"
    )

@pytest.fixture()
def driver(request):
    service_obj = Service(ChromeDriverManager().install())
    
    # Создаем объект опций
    options = Options()

    # Проверяем: если в терминале написали --headless
    headless_mode = request.config.getoption("--headless")

    if headless_mode:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox") # Обязательно для GitHub!
        options.add_argument("--disable-dev-shm-usage") # Обязательно для GitHub!
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    # ВАЖНО: передаем options в драйвер!
    driver_obj = webdriver.Chrome(service=service_obj, options=options)
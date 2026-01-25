import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.pim_page import PimPage
import random

@allure.feature('Тест добавление сотрудника')
@allure.title('Создание сотрудника')
def test_create_employee(driver):
    first_name = f"TestUser_{random.randint(0, 999)}"
    second_name = "Automated"
    last_name = "Mezhen"

    login_page = LoginPage(driver)
    with allure.step('Открыть страницу по ссылке'):
        login_page.open_login_page()
    with allure.step('Авторизация'):    
        login_page.login("Admin", "admin123")
        assert login_page.get_text(login_page.dashboard_header) == "Dashboard"

    main_page = MainPage(driver)
    with allure.step('Открытие вкалдки PIM'):  
        main_page.pim()
        assert main_page.get_text(main_page.dashboard_header) == "PIM"

    pim_page = PimPage(driver)
    with allure.step('Заполнение данных об новом пользователе'):  
        pim_page.click_button_add_employee()
        assert pim_page.get_text(pim_page.title_of_add_employee) == "Add Employee"
        pim_page.input_new_employee(first_name, second_name, last_name)
        assert pim_page.is_success_message_displayed()
    with allure.step('Открытие карточки нового пользователя'): 
        assert pim_page.get_text(pim_page.name_profile) == f"{first_name} {last_name}"



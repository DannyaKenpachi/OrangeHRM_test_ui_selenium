from base_page import BasePage
from selenium.webdriver.common.by import By

class PimPAge(BasePage):

    add_employee_button = (By.XPATH, "//span[text()='Add Employee']")
    first_name_input = (By.XPATH, "//input[@name='firstName']")
    middle_name_input = (By.XPATH, "//input[@name='middleName']")
    last_name_input = (By.XPATH, "//input[@name='lastName']")
    save_button = (By.XPATH, "//button[contains(text(), 'Save')]")

    success_message = (By.XPATH, '//div[#oxd-toaster_1]')

    name_profile = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']")

    def click_button_add_employee(self):
        self.click(self.add_employee_button)
    
    def input_new_employee(self, first_name, middle_name, last_name):
        self.set_text(self.first_name_input, first_name)
        self.set_text(self.middle_name_input, middle_name)
        self.set_text(self.last_name_input, last_name)
        self.click(self.save_button)

    def get_prodile_name(self):
        return self.get_text(self.name_profile)

    




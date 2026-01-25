from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PimPage(BasePage):

    add_employee_button = (By.XPATH, "//a[text()='Add Employee']")
    title_of_add_employee = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
    first_name_input = (By.XPATH, "//input[@name='firstName']")
    middle_name_input = (By.XPATH, "//input[@name='middleName']")
    last_name_input = (By.XPATH, "//input[@name='lastName']")
    save_button = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

    success_message = (By.XPATH, "//div[@id = 'oxd-toaster_1']")

    name_profile = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 --strong']")

    def click_button_add_employee(self):
        self.click(self.add_employee_button)
    
    def input_new_employee(self, first_name, middle_name, last_name):
        self.set_text(self.first_name_input, first_name)
        self.set_text(self.middle_name_input, middle_name)
        self.set_text(self.last_name_input, last_name)
        self.click(self.save_button)

    def is_success_message_displayed(self):
        self.find(self.success_message)
        return True

    




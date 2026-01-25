from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    login_button = (By.TAG_NAME, 'button')

    url = 'https://opensource-demo.orangehrmlive.com/'

    def open_login_page(self):
        self.open(self.url)

    def login(self, username, password):
        self.set_text(self.username_field, username)
        self.set_text(self.password_field, password)
        self.click(self.login_button)
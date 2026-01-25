from base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    pim_item = (By.XPATH, '//span[text()="PIM"]')

    def pim(self):
        self.click(self.pim_item)


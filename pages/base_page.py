from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    dashboard_header = (By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]")

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def set_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find(locator)
        self.wait.until(lambda d: element.text != "")
        return element.text
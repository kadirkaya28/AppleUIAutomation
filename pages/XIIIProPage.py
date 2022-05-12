from pages.ConfigurationPage import ConfigurationPage
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class XIIIProPage(BasePage):
    BUY_BUTTON = (By.CLASS_NAME, "ac-ln-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_purchase_button(self):
        self.highlight(self.BUY_BUTTON, "red")
        self.click(self.BUY_BUTTON)
        return ConfigurationPage(self.driver)

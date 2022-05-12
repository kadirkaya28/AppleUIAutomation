from selenium.webdriver.common.by import By
from pages.XIIIProPage import XIIIProPage
from pages.BasePage import BasePage


class IphonePage(BasePage):
    XIII_PRO = (By.CSS_SELECTOR, ".chapternav-item-iphone-13-pro a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def __str__(self):
        return "Test"

    def select_xiii_pro(self):
        self.highlight(self.XIII_PRO, "red")
        self.click(self.XIII_PRO)
        return XIIIProPage(self.driver)

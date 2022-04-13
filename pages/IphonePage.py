from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class IphonePage(BasePage):
    XIII_PRO = (By.CSS_SELECTOR, ".chapternav-item-iphone-13-pro a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

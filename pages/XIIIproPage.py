from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class XIIIproPage(BasePage):
    BUY_BUTTON = (By.CLASS_NAME, "ac-ln-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

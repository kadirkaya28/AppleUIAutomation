from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class MainPage(BasePage):

    IPHONE = (By.CLASS_NAME, "ac-gn-iphone")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigate_to_url()


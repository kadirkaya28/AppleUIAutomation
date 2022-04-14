from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ReviewBagPage(BasePage):
    REMOVE_BUTTON = (By.CLASS_NAME, "rs-iteminfo-remove")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

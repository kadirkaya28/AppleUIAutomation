from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class IphonePage(BasePage):
    # noinspection SpellCheckingInspection
    XIII_PRO = (By.CSS_SELECTOR, ".chapternav-item-iphone-13-pro a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_xiii_pro(self):
        self.highlight(self.XIII_PRO, "red")
        self.click(self.wait_for_visibility(self.XIII_PRO))

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from config.Config import TestData


class MainPage(BasePage):
    IPHONE = (By.CLASS_NAME, "ac-gn-iphone")

    def __init__(self, driver, lang_code=""):
        super().__init__(driver)
        self.driver = driver
        self.navigate_to_url(TestData.BASE_URL + lang_code)

    def click_to_store(self):
        raise NotImplemented

    def click_to_mac(self):
        raise NotImplemented

    def click_to_ipad(self):
        raise NotImplemented

    def click_to_iphone(self):
        self.highlight(self.IPHONE, "red")
        self.click(self.wait_for_visibility(self.IPHONE))

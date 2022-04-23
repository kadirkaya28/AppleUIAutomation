from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ConfigurationPage(BasePage):
    PRO_OR_MAX = (By.NAME, "dimensionScreensize")  # 0: Pro 1: Max
    COLORS = (By.NAME, "dimensionColor")  # 0: Green 1: Silver 2: Gold 3: Graphite 4: Blue
    CAPACITY = (By.NAME, "dimensionCapacity")  # 0:128 1:256 2:512 3:1TB
    CARRIERS = (By.NAME, "carrierModel")  # click index 4 : No Carrier
    NO_TRADE = (By.ID, "noTradeIn")
    PAYMENT_OPTIONS = (By.NAME, "purchase_option")  # click index 1 : One Time Payment
    APPLE_CARE = (By.ID, "applecareplus_59_noapplecare")
    ADD_BUTTON = (By.NAME, "add-to-cart")
    OPTIONS = (By.CLASS_NAME, "rc-dimension-selector-group")
    TAG = (By.TAG_NAME, "div")
    REVIEW_BAG = (By.NAME, "proceed")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def configure_iphone_specs(self, model: int = 1, capacity: int = 3):
        max_phone = self.find_elements(self.PRO_OR_MAX)[model]
        self.click(self.wait_for_presence(max_phone))

        self.click(self.wait_for_presence(self.COLORS))

        capacity_selection = self.find_elements(self.CAPACITY)[capacity]
        self.click(self.wait_for_presence(capacity_selection))

    def configure_additional_options(self, country, carrier: int = 4, payment: int = 1):
        if country == "Turkey":
            return None
        elif country == "USA":
            no_carrier = self.find_elements(self.CARRIERS)[carrier]
            self.click(self.wait_for_presence(no_carrier))

        self.click(self.wait_for_presence(self.NO_TRADE))

        if country != "France":
            payment_option = self.find_elements(self.PAYMENT_OPTIONS)[payment]
            self.click(self.wait_for_presence(payment_option))

        self.click(self.wait_for_presence(self.APPLE_CARE))

    def go_to_bag(self):
        self.highlight(self.ADD_BUTTON, "red")
        self.click(self.wait_for_presence(self.ADD_BUTTON))

        self.highlight(self.REVIEW_BAG, "red")
        self.click(self.wait_for_presence(self.REVIEW_BAG))

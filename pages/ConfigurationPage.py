from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ConfigurationPage(BasePage):
    PRO_OR_MAX = (By.NAME, "dimensionScreensize")  # 0: Pro 1: Max
    COLORS = (By.NAME, "dimensionColor")  # 0: Green 1: Silver 2: Gold 3: Graphite 4: Blue
    CAPACITY = (By.NAME, "dimensionCapacity")  # 0:128 1:256 2:512 3:1TB
    CARRIERS = (By.NAME, "carrierModel")  # click index 4
    NO_TRADE = (By.ID, "noTradeIn")
    PAY = (By.NAME, "purchase_option_group")  # click index 1
    PAYMENT_OPTIONS = (By.NAME, "purchase_option")  # click index 1
    APPLE_CARE = (By.ID, "applecareplus_59_noapplecare")
    ADD_BUTTON = (By.NAME, "add-to-cart")
    OPTIONS = (By.CLASS_NAME, "rc-dimension-selector-group")
    TAG = (By.TAG_NAME, "div")
    REVIEW_BAG = (By.NAME, "proceed")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

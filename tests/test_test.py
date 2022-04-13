from pages.ConfigurationPage import ConfigurationPage
from pages.IphonePage import IphonePage
from pages.MainPage import MainPage
from pages.ReviewBagPage import ReviewBagPage
from pages.XIIIproPage import XIIIproPage
from tests import BaseTest


class Test(BaseTest):

    def test_test(self):
        main_page = MainPage(self.driver)
        iphone_page = IphonePage(self.driver)
        pro_page = XIIIproPage(self.driver)
        conf_page = ConfigurationPage(self.driver)
        rev_bag_page = ReviewBagPage(self.driver)

        main_page.highlight(main_page.IPHONE, "red")
        main_page.click_visibility(main_page.IPHONE)

        iphone_page.highlight(iphone_page.XIII_PRO, "red")
        iphone_page.click_visibility(iphone_page.XIII_PRO)

        pro_page.highlight(pro_page.BUY_BUTTON, "red")
        pro_page.click_visibility(pro_page.BUY_BUTTON)

        max_phone = conf_page.find_elements(conf_page.PRO_OR_MAX)[1]
        conf_page.click_presence(max_phone)

        conf_page.click_presence(conf_page.COLORS)

        capacity = conf_page.find_elements(conf_page.CAPACITY)[3]
        conf_page.click_presence(capacity)

        carrier = conf_page.find_elements(conf_page.CARRIERS)[4]
        conf_page.click_presence(carrier)

        conf_page.click_presence(conf_page.NO_TRADE)

        payment_option = conf_page.find_elements(conf_page.PAYMENT_OPTIONS)[1]
        conf_page.click_presence(payment_option)

        conf_page.click_presence(conf_page.APPLE_CARE)

        conf_page.highlight(conf_page.ADD_BUTTON, "red")
        conf_page.click_presence(conf_page.ADD_BUTTON)

        conf_page.highlight(conf_page.REVIEW_BAG, "red")
        conf_page.click_presence(conf_page.REVIEW_BAG)





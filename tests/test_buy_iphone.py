import pytest

from config.Config import TestData
from pages.ConfigurationPage import ConfigurationPage
from pages.IphonePage import IphonePage
from pages.MainPage import MainPage
from pages.ReviewBagPage import ReviewBagPage
from pages.XIIIproPage import XIIIproPage
from tests import BaseTest


class Test(BaseTest):
    @pytest.mark.parametrize("country, shortcode", TestData.LANG_CODES.items())
    def test_buy_iphone(self, country, shortcode):
        assertion_values = TestData.ASSERTIONS[country]
        print("Apple Automation is Working For This Country:", country)
        main_page = MainPage(self.driver, lang_code=shortcode)
        iphone_page = IphonePage(self.driver)
        pro_page = XIIIproPage(self.driver)
        conf_page = ConfigurationPage(self.driver)
        rev_bag_page = ReviewBagPage(self.driver)

        assert self.driver.title == assertion_values["main_title"]
        main_page.wait(main_page.IPHONE, assertion_values["menu_text"])
        assert main_page.get_element_text(main_page.IPHONE) == assertion_values["menu_text"]

        main_page.highlight(main_page.IPHONE, "red")
        main_page.click_visibility(main_page.IPHONE)

        assert self.driver.title == assertion_values["iphone_title"]
        assert iphone_page.get_element_text(iphone_page.XIII_PRO) == assertion_values["menu_iphone_text"]

        iphone_page.highlight(iphone_page.XIII_PRO, "red")
        iphone_page.click_visibility(iphone_page.XIII_PRO)

        assert self.driver.title == assertion_values["pro_title"]
        assert pro_page.get_element_text(pro_page.BUY_BUTTON) == assertion_values["buy_button"]
        assert pro_page.is_clickable(pro_page.BUY_BUTTON)

        pro_page.highlight(pro_page.BUY_BUTTON, "red")
        pro_page.click_visibility(pro_page.BUY_BUTTON)

        max_phone = conf_page.find_elements(conf_page.PRO_OR_MAX)[1]
        conf_page.click_presence(max_phone)

        conf_page.click_presence(conf_page.COLORS)

        capacity = conf_page.find_elements(conf_page.CAPACITY)[3]
        conf_page.click_presence(capacity)

        if country != "Turkey":
            if country != "United Kingdom" and country != "Deutschland" and country != "Italy" and country != "France" and country != "Spain":
                carrier = conf_page.find_elements(conf_page.CARRIERS)[4]
                conf_page.click_presence(carrier)

            conf_page.click_presence(conf_page.NO_TRADE)

            if country != "France":
                payment_option = conf_page.find_elements(conf_page.PAYMENT_OPTIONS)[1]
                conf_page.click_presence(payment_option)

            conf_page.click_presence(conf_page.APPLE_CARE)

        conf_page.highlight(conf_page.ADD_BUTTON, "red")
        conf_page.click_presence(conf_page.ADD_BUTTON)

        conf_page.highlight(conf_page.REVIEW_BAG, "red")
        conf_page.click_presence(conf_page.REVIEW_BAG)

        rev_bag_page.highlight(rev_bag_page.REMOVE_BUTTON, "red")
        rev_bag_page.click_presence(rev_bag_page.REMOVE_BUTTON)

        assert assertion_values["page_source"] in self.driver.page_source

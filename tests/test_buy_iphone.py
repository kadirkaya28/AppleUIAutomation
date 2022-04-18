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
        assert main_page.get_element_text(main_page.IPHONE) == assertion_values["menu_text"]
        main_page.click_to_iphone()

        assert self.driver.title == assertion_values["iphone_title"]
        assert iphone_page.get_element_text(iphone_page.XIII_PRO) == assertion_values["menu_iphone_text"]
        iphone_page.select_xii_pro()

        assert self.driver.title == assertion_values["pro_title"]
        assert pro_page.get_element_text(pro_page.BUY_BUTTON) == assertion_values["buy_button"]
        assert pro_page.is_clickable(pro_page.BUY_BUTTON)
        pro_page.click_purchase_button()

        conf_page.configure_iphone_specs()

        conf_page.configure_additional_options(country)

        conf_page.add_and_go_to_bag()

        rev_bag_page.remove_iphone()
        assert assertion_values["page_source"] in self.driver.page_source

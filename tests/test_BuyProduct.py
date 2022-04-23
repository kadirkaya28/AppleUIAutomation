from pages.ConfigurationPage import ConfigurationPage
from pages.ReviewBagPage import ReviewBagPage
from pages.XIIIProPage import XIIIProPage
from pages.IphonePage import IphonePage
from pages.MainPage import MainPage
from config.Config import TestData
from tests import BaseTest
import pytest


class TestBuyProduct(BaseTest):

    @pytest.mark.parametrize("country, shortcode", TestData.LANG_CODES.items())
    def test_buy_iphone(self, country, shortcode):
        print("Apple Automation is Working For This Country:", country)
        assertion_values = TestData.ASSERTIONS.get(country)

        main_page = MainPage(self.driver, lang_code=shortcode)
        iphone_page = IphonePage(self.driver)
        pro_page = XIIIProPage(self.driver)
        conf_page = ConfigurationPage(self.driver)
        rev_bag_page = ReviewBagPage(self.driver)

        assert main_page.get_title() == assertion_values.get("main_title")
        assert main_page.get_element_text(main_page.IPHONE) == assertion_values.get("menu_text")
        main_page.click_to_iphone()

        assert iphone_page.get_title() == assertion_values.get("iphone_title")
        assert iphone_page.get_element_text(iphone_page.XIII_PRO) == assertion_values.get("menu_iphone_text")
        iphone_page.select_xiii_pro()

        assert pro_page.get_title() == assertion_values.get("pro_title")
        assert pro_page.get_element_text(pro_page.BUY_BUTTON) == assertion_values.get("buy_button")
        assert pro_page.is_clickable(pro_page.BUY_BUTTON)
        pro_page.click_purchase_button()

        conf_page.configure_iphone_specs()
        conf_page.configure_additional_options(country)
        conf_page.go_to_bag()

        rev_bag_page.remove_iphone()
        assert assertion_values.get("page_source") in rev_bag_page.get_element_text(rev_bag_page.BODY)

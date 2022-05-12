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

        self.EnsureThat.is_same(main_page.get_title(), assertion_values.get("main_title"))
        self.EnsureThat.is_same(main_page.get_element_text(main_page.IPHONE), assertion_values.get("menu_text"))
        iphone_page = main_page.click_to_iphone()

        self.EnsureThat.is_same(iphone_page.get_title(), assertion_values.get("iphone_title"))
        self.EnsureThat.is_same(iphone_page.get_element_text(iphone_page.XIII_PRO), assertion_values.get("menu_iphone_text"))
        pro_page = iphone_page.select_xiii_pro()

        self.EnsureThat.is_same(pro_page.get_title(), assertion_values.get("pro_title"))
        self.EnsureThat.is_same(pro_page.get_element_text(pro_page.BUY_BUTTON), assertion_values.get("buy_button"))
        self.EnsureThat.is_true(pro_page.is_clickable(pro_page.BUY_BUTTON))
        conf_page = pro_page.click_purchase_button()

        conf_page.configure_iphone_specs()
        conf_page.configure_additional_options(country)
        rev_bag_page = conf_page.go_to_bag()

        rev_bag_page.remove_iphone()
        self.EnsureThat.text_in(assertion_values.get("page_source"), rev_bag_page.get_element_text(rev_bag_page.BODY))

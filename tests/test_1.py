import pytest
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class Test_1:

    def test_login(self, open_browser, close_browser):
        login_page = open_browser
        login_page.type_login()
        login_page.type_password()
        login_page.click_on_login()
        assert not login_page.is_login_button_present()

        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_product_page_correct()
        assert products_page.is_menu_present()


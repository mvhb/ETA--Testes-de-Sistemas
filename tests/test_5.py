from Pages.CheckoutCompletePage import CheckoutCompletePage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutPage import CheckoutPage
from Pages.ProductsPage import ProductsPage


class Test_5():

    def test_finish_a_product_buy(self, open_browser, efetuar_login, close_browser):
        products_page = efetuar_login
        products_page = ProductsPage(products_page.driver)
        products_page.add_sauce_labs_backpack()
        checkout_page = CheckoutPage(products_page.driver)
        checkout_page.click_on_checkout_icon()
        checkout_page.click_on_checkout_button()
        assert checkout_page.is_checkout_page_correct()
        checkout_page.type_in_first_name_field("Marcos")
        checkout_page.type_in_last_name_field("Borges")
        checkout_page.type_in_zip_postal_code_field("513260271")
        checkout_page.click_on_continue()
        checkout_overview_page = CheckoutOverviewPage(checkout_page.driver)
        assert checkout_overview_page.is_checkout_overview_page_correct()
        assert checkout_overview_page.get_product_price() == "$29.99", "Incorrect price value"
        assert checkout_overview_page.get_cart_quantity() == "1", "Incorrect cart quantity"
        assert checkout_overview_page.get_product_name() == "Sauce Labs Backpack", "Incorrect product name"
        checkout_overview_page.click_on_finish()
        checkout_complete_page = CheckoutCompletePage(checkout_page.driver)
        assert checkout_complete_page.is_checkout_complete_page_correct()
        assert checkout_complete_page.get_thank_you_message() == "THANK YOU FOR YOUR ORDER"

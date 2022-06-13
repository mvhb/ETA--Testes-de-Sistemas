from Pages.CartPage import CartPage
from Pages.CheckoutCompletePage import CheckoutCompletePage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutPage import CheckoutPage
from Pages.ProductsPage import ProductsPage


class Test_6():

    def test_add_a_product_to_cart(self, open_browser, efetuar_login, close_browser):
        products_page = efetuar_login
        products_page = ProductsPage(products_page.driver)
        products_page.add_sauce_labs_backpack()
        assert products_page.is_remove_button_present()
        assert products_page.get_remove_button_text() == "REMOVE"
        checkout_page = CheckoutPage(products_page.driver)
        assert checkout_page.get_shopping_cart_text() == "1"
        checkout_page.click_on_checkout_icon()
        cart_page = CartPage(products_page.driver)
        cart_page.is_cart_page_correct()
        assert cart_page.get_product_price() == "$29.99", "Incorrect price value"
        assert cart_page.get_cart_quantity() == "1", "Incorrect cart quantity"
        assert cart_page.get_product_name() == "Sauce Labs Backpack", "Incorrect product name"

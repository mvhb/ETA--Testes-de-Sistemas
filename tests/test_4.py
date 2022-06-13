from Pages.CheckoutPage import CheckoutPage


class Test_4:

    def test_check_checkout_message(self, open_browser, efetuar_login, add_first_product_of_the_list, close_browser):
        checkout_page = add_first_product_of_the_list
        checkout_page = CheckoutPage(checkout_page.driver)
        checkout_page.click_on_checkout_icon()
        checkout_page.click_on_checkout_button()
        assert checkout_page.is_checkout_page_correct()
        checkout_page.click_on_continue()
        assert checkout_page.get_error_message() == "Error: First Name is required"

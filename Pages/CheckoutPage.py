from selenium.webdriver.common.by import By

from Pages.MainPage import MainPage


class CheckoutPage(MainPage):

    TITLE = "CHECKOUT: YOUR INFORMATION"
    CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"

    checkout_icon = "shopping_cart_container"
    checkout_button = "checkout"
    continue_button = "continue"
    error_message = "error-message-container"
    first_name_field = "first-name"
    last_name_field = "last-name"
    zip_postal_code_field = "postal-code"
    shopping_cart_span = "shopping_cart_badge"


    def __init__(self, driver):
        super(CheckoutPage, self).__init__(driver=driver)

    def click_on_checkout_icon(self):
        self.driver.find_element(By.ID, self.checkout_icon).click()

    def click_on_checkout_button(self):
        self.driver.find_element(By.ID, self.checkout_button).click()

    def is_checkout_page_correct(self):
        return self.is_page_correct(url=self.CHECKOUT_PAGE_URL, title=self.TITLE)

    def click_on_continue(self):
        self.driver.find_element(By.ID, self.continue_button).click()

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.error_message).text

    def type_in_first_name_field(self, first_name):
        self.driver.find_element(By.ID, self.first_name_field).send_keys(first_name)

    def type_in_last_name_field(self, last_name):
        self.driver.find_element(By.ID, self.last_name_field).send_keys(last_name)

    def type_in_zip_postal_code_field(self, zip_postal_code):
        self.driver.find_element(By.ID, self.zip_postal_code_field).send_keys(zip_postal_code)

    def get_shopping_cart_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.shopping_cart_span).text

from selenium.webdriver.common.by import By

from Pages.MainPage import MainPage


class CheckoutCompletePage(MainPage):

    TITLE = "CHECKOUT: COMPLETE!"
    CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-complete.html"

    thank_you_message = "complete-header"

    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver=driver)

    def is_checkout_complete_page_correct(self):
        return self.is_page_correct(url=self.CHECKOUT_PAGE_URL, title=self.TITLE)

    def get_thank_you_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.thank_you_message).text

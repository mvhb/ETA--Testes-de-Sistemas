from selenium.webdriver.common.by import By

from Pages.MainPage import MainPage


class CartPage(MainPage):

    TITLE = "YOUR CART"
    PAGE_URL = "https://www.saucedemo.com/cart.html"

    item_price = "inventory_item_price"
    cart_quantity = "cart_quantity"
    product_name = "inventory_item_name"

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def is_cart_page_correct(self):
        return self.is_page_correct(url=self.PAGE_URL, title=self.TITLE)

    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, self.item_price).text

    def get_cart_quantity(self):
        return self.driver.find_element(By.CLASS_NAME, self.cart_quantity).text

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, self.product_name).text

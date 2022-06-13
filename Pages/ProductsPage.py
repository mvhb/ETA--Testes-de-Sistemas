from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.MainPage import MainPage


class ProductsPage(MainPage):
    PRODUCT_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    TITLE = "PRODUCTS"
    menu = "react-burger-menu-btn"
    sauce_labs_backpack_product = "add-to-cart-sauce-labs-backpack"
    first_product_of_the_list = "inventory_item"
    item_button = "btn_primary"
    sauce_labs_backpack = "add-to-cart-sauce-labs-backpack"
    remove_button = "remove-sauce-labs-backpack"

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_menu_present(self):
        try:
            self.driver.find_element(By.ID, self.menu)
            return True
        except NoSuchElementException:
            return False

    def is_product_page_correct(self):
        return self.is_page_correct(url=self.PRODUCT_PAGE_URL, title=self.TITLE)

    def add_first_product_of_the_list(self):
        product_card = self.driver.find_element(By.CLASS_NAME, self.first_product_of_the_list)
        product_card.find_element(By.CLASS_NAME, self.item_button).click()

    def add_sauce_labs_backpack(self):
        self.driver.find_element(By.ID, self.sauce_labs_backpack).click()

    def is_remove_button_present(self):
        try:
            self.driver.find_element(By.ID, self.remove_button)
            return True
        except NoSuchElementException:
            return False

    def get_remove_button_text(self):
        return self.driver.find_element(By.ID, self.remove_button).text

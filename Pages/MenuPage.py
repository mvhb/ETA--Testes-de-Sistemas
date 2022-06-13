import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.MainPage import MainPage


class MenuPage(MainPage):

    SHORT_SECONDS = 5

    menu_dropdown = "react-burger-menu-btn"
    logout_option = "logout_sidebar_link"
    all_menu = "bm-item-list"

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def click_on_menu_dropdown(self):
        self.driver.find_element(By.ID, self.menu_dropdown).click()

    def click_on_logout_option(self):
        element = WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.ID, self.logout_option)))
        element.click()

    def is_menu_displayed(self):
        try:
            WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.all_menu)))
            return True
        except TimeoutException:
            return False


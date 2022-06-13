from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Pages.MainPage import MainPage


class LoginPage(MainPage):
    URL = "https://www.saucedemo.com/"

    login = "user-name"
    password = "password"
    login_button = "login-button"

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser)

    def open_page(self):
        self.driver.get(self.URL)

    def type_login(self, username="standard_user"):
        user_name_field = self.driver.find_element(By.ID, self.login)
        user_name_field.send_keys(username)

    def type_password(self, password="secret_sauce"):
        password_field = self.driver.find_element(By.ID, self.password)
        password_field.send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.ID, self.login_button).click()


    def is_login_button_present(self):
        try:
            self.driver.find_element(By.ID, self.login_button)
            return True
        except NoSuchElementException:
            return False

    def is_login_page_correct(self):
        return self.is_page_correct(url=self.URL)

import pytest
from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage


class Test_3:

    def test_logout(self, efetuar_login, close_browser):
        login_page = efetuar_login
        menu_page = MenuPage(login_page.driver)
        menu_page.click_on_menu_dropdown()
        assert menu_page.is_menu_displayed(), "Menu não está sendo exibido na tela"
        menu_page.click_on_logout_option()
        assert login_page.is_login_page_correct(), "URL não é a de login"


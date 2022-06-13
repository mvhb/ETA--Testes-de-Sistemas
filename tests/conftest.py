import pytest

from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run the tests")

@pytest.fixture
def browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    return selected_browser

@pytest.fixture()
def open_browser(browser):
    login_page = LoginPage(browser="chrome")
    login_page.open_page()
    yield login_page

@pytest.fixture()
def efetuar_login(open_browser):
    login_page = open_browser
    login_page.type_login()
    login_page.type_password()
    login_page.click_on_login()
    yield login_page


@pytest.fixture()
def add_first_product_of_the_list(open_browser):
    product_page = ProductsPage(open_browser.driver)
    product_page.add_first_product_of_the_list()
    yield product_page

@pytest.fixture()
def close_browser(open_browser):
    yield
    login_page = open_browser
    login_page.close_page()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import LoginPage, ProductsPage, CartPage, CheckoutPage


class TestSauceDemoCheckout:
    @pytest.fixture(autouse=True)
    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # для запуска без GUI
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

        yield

        self.driver.quit()

    def test_checkout_total_price(self):
        username = "standard_user"
        password = "secret_sauce"
        first_name = "John"
        last_name = "Doe"
        postal_code = "12345"
        expected_total = "58.29"

        login_page = LoginPage(self.driver)
        products_page = login_page.open() \
            .enter_username(username) \
            .enter_password(password) \
            .click_login()

        products_page.add_product_to_cart("Sauce Labs Backpack") \
            .add_product_to_cart("Sauce Labs Bolt T-Shirt") \
            .add_product_to_cart("Sauce Labs Onesie")

        cart_page = products_page.go_to_cart()
        checkout_page = cart_page.click_checkout()

        checkout_page.fill_shipping_info(first_name, last_name, postal_code) \
            .click_continue()

        actual_total = checkout_page.get_total_price()

        assert actual_total == expected_total, \
            f"Expected total: ${expected_total}, but got: ${actual_total}"
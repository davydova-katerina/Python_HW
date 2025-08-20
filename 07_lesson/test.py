import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSauceDemo:
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

    def test_checkout_total_amount(self):
        # Создание объекта страницы авторизации
        login_page = LoginPage(self.driver)

        inventory_page = (login_page.open()
                          .enter_username("standard_user")
                          .enter_password("secret_sauce")
                          .click_login())

        (inventory_page.add_item_to_cart("Sauce Labs Backpack")
         .add_item_to_cart("Sauce Labs Bolt T-Shirt")
         .add_item_to_cart("Sauce Labs Onesie"))

        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.click_checkout()

        (checkout_page.fill_shipping_info("John", "Doe", "12345")
         .click_continue())

        total_amount = checkout_page.get_total_amount()

        assert total_amount == "58.29", f"Expected $58.29, but got ${total_amount}"
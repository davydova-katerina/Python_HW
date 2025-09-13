import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Page import LoginPage, ProductsPage, CartPage, CheckoutPage
import allure


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
class TestSauceDemoCheckout:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Фикстура для настройки тестового окружения."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

        yield

        self.driver.quit()

    @allure.title("Проверка итоговой стоимости заказа")
    @allure.description("Тест проверяет корректность расчета итоговой стоимости при добавлении трех товаров в корзину")
    def test_checkout_total_price(self):
        username = "standard_user"
        password = "secret_sauce"
        first_name = "John"
        last_name = "Doe"
        postal_code = "12345"
        expected_total = "58.29"

        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(self.driver)
            products_page = login_page.open() \
                .enter_username(username) \
                .enter_password(password) \
                .click_login()

        with allure.step("Добавление товаров в корзину"):
            products_page.add_product_to_cart("Sauce Labs Backpack") \
                .add_product_to_cart("Sauce Labs Bolt T-Shirt") \
                .add_product_to_cart("Sauce Labs Onesie")

        with allure.step("Переход к оформлению заказа"):
            cart_page = products_page.go_to_cart()
            checkout_page = cart_page.click_checkout()

        with allure.step("Заполнение информации о доставке"):
            checkout_page.fill_shipping_info(first_name, last_name, postal_code) \
                .click_continue()

        with allure.step("Проверка итоговой стоимости"):
            actual_total = checkout_page.get_total_price()

            with allure.step(f"Ожидаемая сумма: ${expected_total}, Фактическая сумма: ${actual_total}"):
                assert actual_total == expected_total, \
                    f"Expected total: ${expected_total}, but got: ${actual_total}"
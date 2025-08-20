from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)
        return self

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        return ProductsPage(self.driver)


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        product_map = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }

        if product_name in product_map:
            add_button = self.driver.find_element(By.ID, product_map[product_name])
            add_button.click()
        return self

    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items_count(self):
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge[0].text) if cart_badge else 0

    def click_checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_shipping_info(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

        return self

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        return self

    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.split("$")[1]

    def finish_checkout(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        return self
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
            EC.element_to_be_clickable((By.ID, "user-name"))
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
        return InventoryPage(self.driver)


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        add_button.click()
        return self

    def go_to_cart(self):
        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [item.text for item in cart_items]

    def click_checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_shipping_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)

        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        return self

    def get_total_amount(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.split("$")[1]

    def finish_checkout(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        return self
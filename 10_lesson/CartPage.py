from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple, List
import allure

class CartPage(Page):
    """Страница корзины Sauce Demo."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> 'CheckoutPage':
        """
        Нажимает кнопку оформления заказа.

        Returns:
            CheckoutPage: Экземпляр страницы оформления заказа
        """
        self.click_element(self.checkout_button)
        return CheckoutPage(self.driver)

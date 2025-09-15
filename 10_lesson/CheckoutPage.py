from Page import Page
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

class CheckoutPage(Page):
    """Страница оформления заказа Sauce Demo."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить информацию о доставке")
    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """
        Заполняет информацию о доставке.

        Args:
            first_name (str): Имя
            last_name (str): Фамилия
            postal_code (str): Почтовый индекс

        Returns:
            CheckoutPage: Экземпляр страницы оформления заказа
        """
        self.enter_text(self.first_name_field, first_name)
        self.enter_text(self.last_name_field, last_name)
        self.enter_text(self.postal_code_field, postal_code)
        return self

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> 'CheckoutPage':
        """
        Нажимает кнопку продолжения.

        Returns:
            CheckoutPage: Экземпляр страницы оформления заказа
        """
        self.click_element(self.continue_button)
        return self

    @allure.step("Получить итоговую цену")
    def get_total_price(self) -> str:
        """
        Получает итоговую цену заказа.

        Returns:
            str: Итоговая цена
        """
        element = self.find_element(self.total_price)
        return element.text.replace("Total: $", "")
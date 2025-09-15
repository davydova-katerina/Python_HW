from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple
import allure

class LoginPage(Page):
    """Страница авторизации Sauce Demo."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: Экземпляр страницы авторизации
        """
        self.driver.get(self.url)
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> 'LoginPage':
        """
        Вводит имя пользователя.

        Args:
            username (str): Имя пользователя

        Returns:
            LoginPage: Экземпляр страницы авторизации
        """
        self.enter_text(self.username_field, username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> 'LoginPage':
        """
        Вводит пароль.

        Args:
            password (str): Пароль пользователя

        Returns:
            LoginPage: Экземпляр страницы авторизации
        """
        self.enter_text(self.password_field, password)
        return self

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> 'ProductsPage':
        """
        Нажимает кнопку входа.

        Returns:
            ProductsPage: Экземпляр страницы продуктов
        """
        self.click_element(self.login_button)
        return ProductsPage(self.driver)
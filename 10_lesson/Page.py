from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class Page:
    """Базовый класс для всех страниц веб-приложения."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр страницы.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: tuple[By, str]) -> WebElement:
        """
        Находит элемент на странице.

        Args:
            locator (tuple[By, str]): Локатор элемента (стратегия, значение)

        Returns:
            WebElement: Найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple[By, str]) -> None:
        """
        Кликает по элементу.

        Args:
            locator (tuple[By, str]): Локатор элемента
        """
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator: tuple[By, str], text: str) -> None:
        """
        Вводит текст в поле ввода.

        Args:
            locator (tuple[By, str]): Локатор поля ввода
            text (str): Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
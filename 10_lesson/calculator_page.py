from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Optional


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.url = "https://example.com/calculator"  # Замените на реальный URL

        # Локаторы элементов
        self.RESULT_FIELD = (By.ID, "result")
        self.DELAY_INPUT = (By.ID, "delay")
        self.BUTTON_7 = (By.ID, "btn7")
        self.BUTTON_8 = (By.ID, "btn8")
        self.PLUS_BUTTON = (By.ID, "plus")
        self.EQUALS_BUTTON = (By.ID, "equals")

    def open(self) -> 'CalculatorPage':
        """
        Открыть страницу калькулятора.

        Returns:
            CalculatorPage: Текущий экземпляр страницы
        """
        self.driver.get(self.url)
        return self

    def set_delay(self, delay: int) -> 'CalculatorPage':
        """
        Установить задержку вычислений.

        Args:
            delay: Время задержки в секундах

        Returns:
            CalculatorPage: Текущий экземпляр страницы
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(delay))
        return self

    def click_button_7(self) -> 'CalculatorPage':
        """
        Нажать кнопку '7'.

        Returns:
            CalculatorPage: Текущий экземпляр страницы
        """
        self.driver.find_element(*self.BUTTON_7).click()
        return self

    def click_button_8(self) -> 'CalculatorPage':
        """
        Нажать кнопку '8'.

        Returns:
            CalculatorPage: Текущий экземпляр страницы
        """
        self.driver.find_element(*self.BUTTON_8).click()
        return self

    def click_plus(self) -> 'CalculatorPage':
        """
        Нажать кнопку '+' (сложение).

        Returns:
            CalculatorPage: Текущий экземпляр страницы
        """
        self.driver.find_element(*self.PLUS_BUTTON).click()
        return self

    def click_equals(self) -> 'CalculatorPage':
        """
        Нажать кнопку '=' (равно).

        Returns:
            CalculatorPage: Текущий экземпляр страницы
        """
        self.driver.find_element(*self.EQUALS_BUTTON).click()
        return self

    def get_result(self, timeout: int = 10) -> str:
        """
        Получить результат вычислений.

        Args:
            timeout: Максимальное время ожидания в секундах

        Returns:
            str: Текст результата вычислений
        """
        wait = WebDriverWait(self.driver, timeout)
        result_element = wait.until(
            EC.visibility_of_element_located(self.RESULT_FIELD)
        )
        return result_element.text

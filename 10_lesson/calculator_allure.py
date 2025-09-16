import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


class TestCalculator:

    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации и закрытия драйвера."""
        with allure.step("Инициализация WebDriver"):
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            yield driver

        with allure.step("Закрытие браузера"):
            driver.quit()

    @allure.title("Тест калькулятора с задержкой")
    @allure.description("Проверка работы калькулятора с установленной задержкой вычислений")
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("calculator", "delay", "regression")
    def test_calculator_with_delay(self, driver):
        """Тестирование вычисления 7 + 8 с задержкой 45 секунд."""

        calculator_page = CalculatorPage(driver)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Ввод выражения 7 + 8"):
            calculator_page.click_button_7() \
                .click_plus() \
                .click_button_8()

        with allure.step("Нажатие кнопки равно"):
            calculator_page.click_equals()

        with allure.step("Получение результата с ожиданием 50 секунд"):
            result = calculator_page.get_result(timeout=50)

        with allure.step("Проверка результата вычислений"):
            expected_result = "15"
            assert result == expected_result, (
                f"Ожидался результат '{expected_result}', но получено '{result}'"
            )

        allure.dynamic.description(f"Проверено: 7 + 8 = {result}")
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_calculator_with_delay(self, driver):
        calculator_page = CalculatorPage(driver)

        calculator_page.open() \
            .set_delay(45) \
            .click_button_7() \
            .click_plus() \
            .click_button_8() \
            .click_equals()

        result = calculator_page.get_result(timeout=50)

        assert result == "15", f"Ожидался результат '15', но получено '{result}'"
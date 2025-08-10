from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def input_field_interaction():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

        input_field.send_keys("Sky")

        input_field.clear()

        input_field.send_keys("Pro")

        input("Нажмите Enter для закрытия браузера...")

    finally:
        driver.quit()


if __name__ == "__main__":
    input_field_interaction()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

def test_form_submission(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_id, value in form_data.items():
        field = browser.find_element(By.ID, field_id)
        field.clear()
        field.send_keys(value)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    zip_code_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code должно быть подсвечено красным"

    green_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} должно быть подсвечено зеленым"
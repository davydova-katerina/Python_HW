import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_saucedemo_checkout(browser):
    browser.get("https://www.saucedemo.com/")

    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        add_to_cart_button.click()

    cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Екатерина")

    last_name = browser.find_element(By.ID, "last-name")
    last_name.send_keys("Давыдова")

    postal_code = browser.find_element(By.ID, "postal-code")
    postal_code.send_keys("123456")

    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()

    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    assert total_text == "Total: $58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_text}"
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
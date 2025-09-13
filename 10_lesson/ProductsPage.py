class ProductsPage(Page):
    """Страница продуктов Sauce Demo."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.product_add_button = (By.XPATH,
                                   "//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить продукт '{product_name}' в корзину")
    def add_product_to_cart(self, product_name: str) -> 'ProductsPage':
        """
        Добавляет продукт в корзину.

        Args:
            product_name (str): Название продукта

        Returns:
            ProductsPage: Экземпляр страницы продуктов
        """
        locator = (By.XPATH, self.product_add_button[1].format(product_name=product_name))
        self.click_element(locator)
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> 'CartPage':
        """
        Переходит в корзину.

        Returns:
            CartPage: Экземпляр страницы корзины
        """
        self.click_element(self.cart_icon)
        return CartPage(self.driver)
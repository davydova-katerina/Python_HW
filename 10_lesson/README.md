# Тестовый проект калькулятора

Проект для автоматизированного тестирования веб-калькулятора с использованием Selenium и Allure.

## Структура проекта
10_lesson/
├── calculator_allure.py # Тесты с Allure разметкой
├── calculator_page.py # Page Object модель калькулятора
├── CartPage.py # Page Object модель корзины
├── CheckoutPage.py # Page Object модель оформления заказа
├── LoginPage.py # Page Object модель авторизации
├── Page.py # Базовый класс Page Object
├── page_allure.py # Тесты с Allure разметкой для страниц
├── ProductsPage.py # Page Object модель страницы продуктов
└── README.md # Документация

## Запуск тестов с сохранением результатов
pytest calculator_allure.py --alluredir=./allure-results
# или
pytest page_allure.py --alluredir=./allure-results

## Генерация отчета
allure generate ./allure-results -o ./allure-report --clean

## Просмотр отчета
allure open ./allure-report
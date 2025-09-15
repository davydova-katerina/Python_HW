# Тестовый проект калькулятора

Проект для автоматизированного тестирования веб-калькулятора с использованием Selenium и Allure.

## Структура проекта
project/
├── tests/
│ └── test_calculator.py # Тесты с Allure разметкой
├── pages/
│ └── calculator_page.py # Page Object модель
├── requirements.txt # Зависимости
└── README.md # Документация

# Запуск тестов с сохранением результатов
pytest tests/test_calculator.py --alluredir=./allure-results

# Генерация отчета
allure generate ./allure-results -o ./allure-report --clean

# Просмотр отчета
allure open ./allure-report
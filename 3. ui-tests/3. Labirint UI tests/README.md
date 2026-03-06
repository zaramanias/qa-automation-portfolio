# ENGLISH

## UI Tests for `Labirint` Online Store

### Project Description

This is a small educational project for testing the **Labirint online bookstore website** using **Python**, **Pytest**, and **Selenium WebDriver**.

The project tests basic user scenarios of the website:

- searching for books
- adding items to the cart
- removing items from the cart using the "-" button
- opening the product page
- clearing the cart
- restoring removed items

A `LabirintPage` class is implemented to interact with the website using Selenium WebDriver.  
Automated tests validate that UI functionality works correctly.

---

### Tech Stack

- Python
- Pytest
- Selenium WebDriver
- Allure
- WebDriverWait

---

### Project Structure
```bash
.
├── test_ui_page.py # page object class
├── test_ui.py # automated tests
└── README.md
```
---

### Page Object Class

The `LabirintPage` provides methods for working with the website:

- `search_book()` — search for a book
- `add_to_cart()` — add a product to the cart
- `remove_from_cart()` — remove a product using the "-" button
- `open_product()` — open a product page
- `clear_cart()` — clear the cart
- `restore_items()` — restore removed items

---

### Automated Tests

The project includes the following tests:

- `test_search_book()` — verifies book search functionality
- `test_add_to_cart()` — verifies adding products to the cart
- `test_remove_from_cart()` — verifies removing a product from the cart
- `test_open_product_page()` — verifies opening a product page
- `test_clear_cart()` — verifies clearing the cart
- `test_restore_items()` — verifies restoring removed items

---

### Code Style and Formatting

- Code follows PEP 8 standards
- Page Object Pattern is used to separate page logic and tests
- All test actions are marked using Allure steps
- Explicit waits (WebDriverWait) are used for dynamic elements
- Methods are separated by responsibility

---

### Running Tests

To run UI tests:
pytest -m ui

To run tests with detailed output:
pytest -v


# РУССКИЙ

## UI-тестирование сайта `Labirint`

### Описание проекта

Проект представляет собой автоматизацию UI-тестирования сайта https://www.labirint.ru/ с использованием **Python**, **Selenium WebDriver** и **Pytest**.
Тесты проверяют основные пользовательские сценарии интернет-магазина.

Реализованы проверки:

- Поиск книги
- Добавление товара в корзину
- Удаление товара из корзины через кнопку "-"
- Проверка открытия карточки товара
- Очистка корзины
- Восстановление удалённых товаров
- Логика работы со страницей отделена от тестовых сценариев.

---

### Используемые технологии

- Python 3
- Selenium WebDriver
- Pytest
- Allure
- WebDriverWait

---

### Структура проекта
.
├── test_ui_page.py # класс Page Object
├── test_ui.py # тестовые сценарии
└── README.md

Класс `LabirintPage` содержит методы для работы со страницей сайта:

- `search_book()` — выполнить поиск книги
- `add_to_cart()` — добавить товар в корзину
- `remove_from_cart()` — удалить товар через кнопку "-"
- `open_product()` — открыть карточку товара
- `clear_cart()` — очистить корзину
- `restore_items()` — восстановить удалённые товары

---

### Автоматизированные тесты

В проекте реализованы следующие тесты:

- `test_search_book()` — проверяет поиск книги
- `test_add_to_cart()` — проверяет добавление товара в корзину
- `test_remove_from_cart()` — проверяет удаление товара из корзины
- `test_open_product_page()` — проверяет открытие карточки товара
- `test_clear_cart()` — проверяет очистку корзины
- `test_restore_items()` — проверяет восстановление удалённых товаров

---

### Стиль и форматирование кода

Код соответствует стандарту PEP 8
Используется Page Object Pattern для разделения логики страниц и тестов
Все действия размечены через Allure steps
Используются явные ожидания WebDriverWait
Методы разделены по ответственности

---

### Запуск тестов

Запуск UI-тестов:
pytest -m ui

Запуск с подробным выводом:
pytest -v

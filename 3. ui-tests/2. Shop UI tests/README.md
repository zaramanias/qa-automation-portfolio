# ENGLISH

## UI Tests for `SauceDemo Checkout Total`

### Project Description

This is a small project for testing the **SauceDemo** website using **Python**, **Pytest**, and **Selenium WebDriver**.

The project tests the checkout flow and final cart total calculation:

- opening the shop page
- user authorization
- adding products to the cart
- opening the cart page
- starting checkout
- filling in customer information
- validating the final total amount

A `ShopPage` class is implemented to interact with the product catalog, and a `CartPage` class is implemented to interact with the cart and checkout flow.  
Automated tests validate that the checkout process works correctly.

---

### Tech Stack

- Python
- Pytest
- Selenium WebDriver
- Allure
- Firefox WebDriver

---

### Project Structure
```bash
.
├── ShopPage.py # page object for shop page  
├── CartPage.py # page object for cart and checkout  
├── test_03_shop.py # automated UI tests  
└── README.md
```
---

### Page Object Classes

The `ShopPage` provides methods for working with the shop page:

- `open()` — open the shop page
- `login(username, password)` — authorize user
- `add_to_cart()` — add selected products to the cart

The `CartPage` provides methods for working with the cart and checkout flow:

- `go_to_cart()` — open the cart page
- `checkout()` — click the checkout button
- `fill_checkout_info(first_name, last_name, postal_code)` — fill in customer information
- `get_result()` — get the final total amount

---

### Automated Tests

The project includes the following tests:

- `test_shop_total()` — verifies the final total amount after adding products and completing checkout

---

### Code Style and Formatting

- Code follows PEP 8 standards
- UI actions are encapsulated in separate Page Object classes
- Explicit waits are used for dynamic elements
- Methods are separated by responsibility

---

### Running Tests

To run UI tests:
pytest

To run tests with detailed output:
pytest -v


# РУССКИЙ

## UI-тестирование `SauceDemo Checkout Total`

### Описание проекта

Проект представляет собой автоматизацию тестирования сайта **SauceDemo** с использованием **Python**, **Selenium WebDriver** и **Pytest**.  
Тесты проверяют сценарий оформления заказа и итоговую сумму в корзине.

Реализованы проверки:

- Открытие страницы магазина
- Авторизация пользователя
- Добавление товаров в корзину
- Переход в корзину
- Переход к оформлению заказа
- Заполнение данных покупателя
- Проверка итоговой суммы заказа
- Логика работы со страницами вынесена в отдельные классы.

---

### Используемые технологии

- Python 3
- Selenium WebDriver
- Pytest
- Allure
- Firefox WebDriver

---

### Структура проекта
.
├── ShopPage.py # класс Page Object для магазина  
├── CartPage.py # класс Page Object для корзины и checkout  
├── test_03_shop.py # тестовые сценарии  
└── README.md  

Класс `ShopPage` содержит методы для взаимодействия со страницей магазина:

- `open()` — открыть страницу магазина
- `login(username, password)` — авторизовать пользователя
- `add_to_cart()` — добавить выбранные товары в корзину

Класс `CartPage` содержит методы для взаимодействия с корзиной и оформлением заказа:

- `go_to_cart()` — перейти на страницу корзины
- `checkout()` — нажать кнопку Checkout
- `fill_checkout_info(first_name, last_name, postal_code)` — заполнить данные покупателя
- `get_result()` — получить итоговую сумму заказа

---

### Автоматизированные тесты

В проекте реализованы следующие тесты:

- `test_shop_total()` — проверяет итоговую сумму после добавления товаров и оформления заказа

---

### Стиль и форматирование кода

Код соответствует стандарту PEP 8  
Действия с UI инкапсулированы в отдельных классах Page Object  
Для динамических элементов используются явные ожидания  
Методы разделены по ответственности

---

### Запуск тестов

Запуск всех тестов:
pytest

Запуск с подробным выводом:
pytest -v

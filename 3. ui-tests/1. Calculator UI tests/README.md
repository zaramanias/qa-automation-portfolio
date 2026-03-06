# ENGLISH

## UI Tests for `Slow Calculator`

### Project Description

This is a small project for testing the **Slow Calculator** web page using **Python**, **Pytest**, and **Selenium WebDriver**.

The project tests basic calculator functionality:

- opening the calculator page
- setting calculation delay
- clicking number and operator buttons
- waiting for spinner disappearance
- retrieving the result from the screen
- validating the expected calculation result

A `CalcPage` class is implemented to interact with the calculator page using Selenium WebDriver.  
Automated tests validate that calculator operations work correctly.

---

### Tech Stack

- Python
- Pytest
- Selenium WebDriver
- Allure

---

### Project Structure
```bash
.
├── CalcPage.py # page object class  
├── test_calc.py # automated UI tests  
└── README.md  
```
---

### Page Object Class

The `CalcPage` provides methods for working with the calculator page:

- `open()` — open the calculator page
- `set_delay(delay)` — set operation delay in seconds
- `click_button(symbol)` — click a calculator button by symbol
- `wait_spinner()` — wait until the loading spinner disappears
- `get_result()` — get the result text from the calculator screen
- `calculate()` — calculate the expected result based on entered values

---

### Automated Tests

The project includes the following tests:

- `test_open_calculator()` — verifies opening the calculator page
- `test_set_delay()` — verifies delay input
- `test_addition()` — verifies addition operation
- `test_subtraction()` — verifies subtraction operation
- `test_multiplication()` — verifies multiplication operation
- `test_division()` — verifies division operation
- `test_result_after_spinner()` — verifies the result after spinner disappears

---

### Code Style and Formatting

- Code follows PEP 8 standards
- UI actions are encapsulated in a separate Page Object class
- Explicit waits are used for dynamic elements
- Methods are separated by responsibility

---

### Running Tests

To run UI tests:
pytest

To run tests with detailed output:
pytest -v


# РУССКИЙ

## UI-тестирование `Slow Calculator`

### Описание проекта

Проект представляет собой автоматизацию тестирования веб-страницы **Slow Calculator** с использованием **Python**, **Selenium WebDriver** и **Pytest**.  
Тесты проверяют базовую функциональность калькулятора.

Реализованы проверки:

- Открытие страницы калькулятора
- Установка задержки вычисления
- Нажатие кнопок с цифрами и операторами
- Ожидание исчезновения спиннера
- Получение результата с экрана
- Проверка ожидаемого результата вычисления
- Логика работы со страницей вынесена в отдельный класс.

---

### Используемые технологии

- Python 3
- Selenium WebDriver
- Pytest
- Allure

---

### Структура проекта
.
├── CalcPage.py # класс Page Object  
├── test_calc.py # тестовые сценарии  
└── README.md  

Класс `CalcPage` содержит методы для взаимодействия со страницей калькулятора:

- `open()` — открыть страницу калькулятора
- `set_delay(delay)` — установить задержку выполнения операции
- `click_button(symbol)` — нажать кнопку калькулятора по символу
- `wait_spinner()` — дождаться исчезновения спиннера
- `get_result()` — получить результат с экрана
- `calculate()` — вычислить ожидаемый результат на основе введённых данных

---

### Автоматизированные тесты

В проекте реализованы следующие тесты:

- `test_open_calculator()` — проверяет открытие страницы калькулятора
- `test_set_delay()` — проверяет установку задержки
- `test_addition()` — проверяет операцию сложения
- `test_subtraction()` — проверяет операцию вычитания
- `test_multiplication()` — проверяет операцию умножения
- `test_division()` — проверяет операцию деления
- `test_result_after_spinner()` — проверяет результат после исчезновения спиннера

---

### Стиль и форматирование кода

Код соответствует стандарту PEP 8  
Действия с UI инкапсулированы в отдельном классе Page Object  
Для динамических элементов используются явные ожидания  
Методы разделены по ответственности

---

### Запуск тестов

Запуск всех тестов:
pytest

Запуск с подробным выводом:
pytest -v

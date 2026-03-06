# ENGLISH

## Database Tests for `subject` Table

### Project Description

This is a small educational project for testing a PostgreSQL database using **Python**, **Pytest**, and **SQLAlchemy**.

The project tests basic CRUD operations for the `subject` table:
- retrieving records
- creating new records
- updating records
- deleting records

A `dbclass` class is implemented to interact with the database using SQL queries.  
Automated tests validate that database operations work correctly.

---

### Tech Stack

- Python
- Pytest
- SQLAlchemy
- PostgreSQL
- psycopg

---

### Project Structure
.
├── lesson_9_page.py # database interaction class
├── test_subjects.py # automated tests
└── README.md

---

### Database Class

The `dbclass` provides methods for working with the `subject` table:

- `get_subjects()` — get all records from the table
- `get_subject_by_id(id)` — get record by ID
- `create(title)` — insert a new subject
- `edit(id, title)` — update subject title
- `delete(id)` — delete subject by ID
- `get_max_id()` — get the maximum `subject_id`

---

### Automated Tests

The project includes the following tests:

- `test_get_subjects()` — checks the number of records in the table
- `test_add_new_subj()` — verifies that a new subject can be added
- `test_edit_subj()` — verifies updating a subject
- `test_delete_subj()` — verifies deleting records

---

### Code Style and Formatting

- Code follows PEP 8 standards
- SQL queries are stored separately in a scripts dictionary
- Database operations are wrapped in transactions
- Methods are separated by responsibility

---

### Running Tests

To run database tests:
pytest

To run tests with detailed output:
pytest -v


# РУССКИЙ

## Тестирование базы данных для таблицы `subject`

### Описание проекта

Проект представляет собой автоматизацию тестирования базы данных PostgreSQL с использованием **Python**, **SQLAlchemy** и **Pytest**.
Тесты проверяют CRUD-операции для таблицы `subject`. Реализованы проверки:

- Получение всех записей из таблицы
- Получение записи по ID
- Добавление нового предмета
- Изменение названия предмета
- Удаление записи
- Проверка количества записей до и после операций
- Логика работы с базой данных отделена от тестовых сценариев.

---

### Используемые технологии

- Python 3
- PostgreSQL
- SQLAlchemy
- Pytest
- psycopg

---

### Структура проекта
.
├── lesson_9_page.py # класс для работы с базой данных
├── test_subjects.py # тестовые сценарии
└── README.md

Класс `dbclass` содержит методы для работы с таблицей `subject`:

- `get_subjects()` — получить все записи из таблицы
- `get_subject_by_id(id)` — получить запись по ID
- `create(title)` — добавить новый предмет
- `edit(id, title)` — обновить название предмета
- `delete(id)` — удалить запись по ID
- `get_max_id()` — получить максимальное значение `subject_id`

---

### Автоматизированные тесты

В проекте реализованы следующие тесты:

- `test_get_subjects()` — проверяет количество записей в таблице
- `test_add_new_subj()` — проверяет возможность добавления нового предмета
- `test_edit_subj()` — проверяет обновление названия предмета
- `test_delete_subj()` — проверяет удаление записей

---

### Стиль и форматирование кода

Код соответствует стандарту PEP 8
SQL-запросы вынесены в отдельный словарь scripts
Операции изменения данных выполняются внутри транзакций
Методы разделены по ответственности

---

### Запуск тестов

Запуск всех тестов:
pytest

Запуск с подробным выводом:
pytest -v
# ENGLISH

## API Tests for YouGile 

### Project Description

This is a small project for testing the **YouGile REST API** using **Python**, **Pytest**, and **Requests**.

The project tests basic operations for working with projects in YouGile:

- user authorization
- creating projects
- creating boards
- creating columns
- creating tasks
- retrieving tasks
- retrieving tasks by ID
- soft deleting tasks
- soft deleting projects

A `YougileApi` class is implemented to interact with the API using HTTP requests.  
Automated tests validate that API endpoints work correctly.

---

### Tech Stack

- Python
- Pytest
- Requests
- python-dotenv

---

### Project Structure
.
├── YougilePage.py # API interaction class  
├── test_yougile_proj.py # automated API tests with projects
├── test_yougile_tasks.py # automated API tests with tasks
├── .env # environment variables  
└── README.md  

---

### API Class

The `YougileApi` provides methods for working with the YouGile API:

- `login(login, password, company_id)` — authorize user and get API token
- `get_proj(proj_id=None)` — retrieve projects list or project by ID
- `new_proj(title, user_id)` — create a new project
- `delete_proj(proj_id, deleted=True)` — soft delete project
- `new_board(title, project_id)` — create a board inside a project
- `new_column(title, position, board_id)` — create a column inside a board
- `new_task(title, column_id, description)` — create a task
- `get_tasks()` — retrieve tasks list
- `get_task_by_id(task_id)` — retrieve task by ID
- `delete_task(task_id)` — soft delete task

---

### Automated Tests

The project includes the following tests:

- `test_login()` — verifies successful authorization and token retrieval
- `test_get_projs_positive()` — verifies retrieving the list of projects
- `test_get_proj_with_invalid_id_negative()` — verifies response for invalid project ID
- `test_post_proj_positive()` — verifies successful project creation
- `test_post_proj_bad_title_negative()` — verifies validation error for empty project title
- `test_delete_proj_with_id_positive()` — verifies soft deletion of a project
- `test_delete_all_proj_positive()` — verifies deletion of all projects
- `test_delete_proj_with_invalid_id()` — verifies response for deleting project with invalid ID
- `test_login()` — verifies successful authorization and token retrieval
- `test_create_task()` — verifies project → board → column → task creation and soft deletion
- `test_get_task()` — verifies retrieving tasks and validating task title
- `test_get_task_by_id()` — verifies retrieving task by ID and validating title
- `test_delete_task()` — verifies soft deletion of a task
- `test_delete_proj()` — verifies soft deletion of a project


---

### Code Style and Formatting

- Code follows PEP 8 standards
- API requests are encapsulated in a separate class
- Sensitive data is stored in `.env`
- Methods are separated by responsibility

---

### Running Tests

To run API tests:
pytest

To run tests with detailed output:
pytest -v


# РУССКИЙ

## Тестирование API для YouGile

### Описание проекта

Проект представляет собой автоматизацию тестирования **REST API YouGile** с использованием **Python**, **Requests** и **Pytest**.  
Тесты проверяют основные операции работы с проектами через API.

Реализованы проверки:

- Авторизация пользователя
- Создание проекта
- Создание доски
- Создание колонки
- Создание задачи
- Получение списка задач
- Получение задачи по ID
- Мягкое удаление задачи
- Мягкое удаление проекта
- Проверка работы API при невалидных данных
- Логика работы с API вынесена в отдельный класс.

---

### Используемые технологии

- Python 3
- Requests
- Pytest
- python-dotenv

---

### Структура проекта
.
├── YougilePage.py # класс для работы с API
├── test_yougile_proj.py # тестовые сценарии для вкладки Проекты
├── test_yougile_tasks.py # тестовые сценарии для вкладки Задания
├── .env # переменные окружения
└── README.md

Класс `YougileApi` содержит методы для взаимодействия с API YouGile:

- `login(login, password, company_id)` — авторизация пользователя и получение токена
- `get_proj(proj_id=None)` — получение списка проектов или проекта по ID
- `new_proj(title, user_id)` — создание нового проекта
- `delete_proj(proj_id, deleted=True)` — мягкое удаление проекта
- `new_board(title, project_id)` — создание доски
- `new_column(title, position, board_id)` — создание колонки
- `new_task(title, column_id, description)` — создание задачи
- `get_tasks()` — получение списка задач
- `get_task_by_id(task_id)` — получение задачи по ID
- `delete_task(task_id)` — мягкое удаление задачи

---

### Автоматизированные тесты

В проекте реализованы следующие тесты:

- `test_login()` — проверяет успешную авторизацию и получение токена
- `test_get_projs_positive()` — проверяет получение списка проектов
- `test_get_proj_with_invalid_id_negative()` — проверяет ответ API при невалидном ID
- `test_post_proj_positive()` — проверяет успешное создание проекта
- `test_post_proj_bad_title_negative()` — проверяет ошибку при пустом названии проекта
- `test_delete_proj_with_id_positive()` — проверяет мягкое удаление проекта
- `test_delete_all_proj_positive()` — проверяет удаление всех проектов
- `test_delete_proj_with_invalid_id()` — проверяет ответ API при удалении несуществующего проекта
- `test_create_task()` — проверяет создание проекта → доски → колонки → задачи
- `test_get_task()` — проверяет получение списка задач
- `test_get_task_by_id()` — проверяет получение задачи по ID
- `test_delete_task()` — проверяет мягкое удаление задачи
- `test_delete_proj()` — проверяет мягкое удаление проекта

---

### Стиль и форматирование кода

Код соответствует стандарту PEP 8  
API-запросы инкапсулированы в отдельном классе  
Чувствительные данные хранятся в `.env`  
Методы разделены по ответственности

---

### Запуск тестов

Запуск всех тестов:
pytest

Запуск с подробным выводом:
pytest -v
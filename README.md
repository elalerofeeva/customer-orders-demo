# customer_orders_demo

Учебный мини-проект для лекции **«Основы инструментария: Git, Python, SQL»**.

## Что показывает проект
- Git: структура проекта, коммиты, ветки, push, Pull Request
- Python: переменные, списки, словари, функции, работа с файлами
- Pandas и NumPy: короткий обзор на небольшом наборе данных
- SQL: SELECT, WHERE, JOIN, GROUP BY
- Подключение к БД из Python через sqlite3

## Структура
- `main.py` — точка входа, короткое приветствие
- `file_demo.py` — примеры Python и работа с CSV
- `sql_demo.py` — SQL-запросы к SQLite из Python
- `init_db.py` — создание базы `shop.db` из CSV-файлов
- `data/customers.csv` — данные о клиентах
- `data/orders.csv` — данные о заказах
- `shop.db` — SQLite-база
- `requirements.txt` — зависимости
- `.gitignore` — исключения для Git

## Как запустить
1. Откройте проект в PyCharm
2. Установите зависимости:
   `pip install -r requirements.txt`
3. Создайте базу:
   `python init_db.py`
4. Запускайте по очереди:
   - `python main.py`
   - `python file_demo.py`
   - `python sql_demo.py`

## Идея лекции
Один и тот же проект используется для всех трёх разделов:
- Git хранит историю проекта
- Python реализует обработку данных
- SQL получает и агрегирует данные из БД

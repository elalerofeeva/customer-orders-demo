import sqlite3
from pathlib import Path


DB_PATH = Path("shop.db")


def run_query(connection: sqlite3.Connection, title: str, query: str) -> None:
    print(f"\n=== {title} ===")
    cursor = connection.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    if not DB_PATH.exists():
        print("Файл shop.db не найден. Сначала запустите init_db.py")
        return

    connection = sqlite3.connect(DB_PATH)

    run_query(
        connection,
        "SELECT: все клиенты",
        "SELECT customer_id, name, city FROM customers;"
    )

    run_query(
        connection,
        "WHERE: заказы дороже 1000",
        "SELECT order_id, customer_id, amount, category FROM orders WHERE amount > 1000;"
    )

    run_query(
        connection,
        "JOIN: клиенты и их заказы",
        """
        SELECT customers.name, customers.city, orders.amount, orders.category
        FROM customers
        JOIN orders ON customers.customer_id = orders.customer_id;
        """
    )

    run_query(
        connection,
        "GROUP BY: количество заказов и средняя сумма по категориям",
        """
        SELECT category, COUNT(*) AS total_orders, ROUND(AVG(amount), 2) AS avg_amount
        FROM orders
        GROUP BY category;
        """
    )

    connection.close()


if __name__ == "__main__":
    main()

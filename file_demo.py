from pathlib import Path

import numpy as np
import pandas as pd


def read_customers_csv(file_path: str) -> list[dict]:
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def main():
    project_name = "customer_orders_demo"
    lesson_topics = ["Git", "Python", "SQL"]
    settings = {"database": "shop.db", "data_folder": "data"}

    print("Название проекта:", project_name)
    print("Темы лекции:", lesson_topics)
    print("Настройки:", settings)

    data_dir = Path("data")
    customers_path = data_dir / "customers.csv"
    orders_path = data_dir / "orders.csv"

    print("\nПроверка файловой системы:")
    print("customers.csv существует:", customers_path.exists())
    print("orders.csv существует:", orders_path.exists())

    customers = read_customers_csv(str(customers_path))
    print("\nПервые 2 клиента из CSV:")
    for customer in customers[:2]:
        print(customer)

    orders_df = pd.read_csv(orders_path)
    print("\nТаблица orders.csv:")
    print(orders_df)

    avg_order_amount = orders_df["amount"].mean()
    print("\nСредняя сумма заказа (Pandas):", round(avg_order_amount, 2))

    amounts = np.array(orders_df["amount"])
    print("Суммы заказов как NumPy-массив:", amounts)
    print("Максимальная сумма заказа (NumPy):", amounts.max())


if __name__ == "__main__":
    main()

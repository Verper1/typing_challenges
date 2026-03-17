"""Нужно сделать логику функции parse_receipt и аннотации в ней так, чтобы прошёл тест."""
import datetime


def parse_receipt(raw_receipt: str) -> tuple[int, datetime.date, list[tuple[str, int, float]]]:
    """Парсит строку в кортеж. Пример итога парсинга: (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2), ("Огурцы", 10, 55.3)])."""
    parts = dict(item.split(":", 1) for item in raw_receipt.split())

    receipt_id = int(parts["Кассовый_чек"])

    sale_date = datetime.datetime.strptime(
        parts["Продажа"], "%Y.%m.%d"
    ).date()

    items: list[tuple[str, int, float]] = []

    for item in parts["Позиции"].split(";"):
        name, qty, price = item.strip("()").split(",")

        items.append(
            (name, int(qty), float(price))
        )

    return receipt_id, sale_date, items


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый_чек:12 Продажа:2022.06.12 Позиции:(Молоко,1,32.2);(Огурцы,10,55.3)",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2), ("Огурцы", 10, 55.3)])

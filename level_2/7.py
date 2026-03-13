"""Нужно сделать логику функции calculate_total_spent_for_user и аннотации в ней так, чтобы прошёл тест."""
def calculate_total_spent_for_user(user: tuple[str, int, list]) -> int:
    """Нахождение суммы потраченного пользователем за все покупки."""
    return sum(user[2])


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=("Ilya", 32, [102, 15, 63, 12])) == 192

"""Нужно сделать логику функции calculate_total_spent_for_users и аннотации в ней так, чтобы прошёл тест."""
def calculate_total_spent_for_users(users_ids: set[int],
                                    users_ids_to_users_map: dict[int, tuple[str, int, list]]) -> int:
    """Функция, которая выясняет сколько всего потратили выбранные пользователи."""
    return sum([sum(users_ids_to_users_map[i][2]) for i in users_ids_to_users_map if i in users_ids])


if __name__ == "__main__":
    assert calculate_total_spent_for_users(
        users_ids={3, 6, 12, 15},
        users_ids_to_users_map={
            3: ("Ilya", 32, [102, 15, 63, 12]),
        },
    ) == 192

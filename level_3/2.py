def calculate_total_spent_for_user(user: dict[str, str | int | list[int]]) -> int:
    return sum(user['transactions_sums'])


if __name__ == "__main__":
    assert calculate_total_spent_for_user(
        user={
            "name": "Ilya",
            "age": 32,
            "transactions_sums": [102, 15, 63, 12],
        },
    ) == 192

"""Нужно сделать логику функции is_recovery_code_correct и аннотации в ней так, чтобы прошёл тест."""
import dataclasses
import decimal

@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Transactions:
    """Класс для отработки материала по @dataclasses."""

    def get_transaction_amount(self,
                               transaction_id: int,
                               transactions_amounts_map: dict[int, decimal.Decimal]
                               ) -> decimal.Decimal | None:
        """Метод для нахождения значения (транзакции) в словаре по ключу (id транзакции)."""
        return transactions_amounts_map.get(transaction_id, None)


if __name__ == "__main__":
    example_for_test = Transactions()
    transactions_amounts_map = {
        156: decimal.Decimal("30.6"),
        514: decimal.Decimal("164.1"),
        372: decimal.Decimal("92"),
    }
    assert example_for_test.get_transaction_amount(transaction_id=156, transactions_amounts_map=transactions_amounts_map) == decimal.Decimal("30.6")
    assert example_for_test.get_transaction_amount(transaction_id=1000, transactions_amounts_map=transactions_amounts_map) is None

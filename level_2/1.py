"""Нужно сделать логику функции get_avg_currency_rate и аннотации в ней так, чтобы прошёл тест."""
import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class MathOperations:
    """Класс для отработки материала по @dataclasses."""

    def get_avg_currency_rate(self, rates_history: list[float]) -> float:
        """Нахождение средней арифметической в листе из чисел с плавающей точкой."""
        avg_currency = round(sum(rates_history) / len(rates_history), 1)
        return avg_currency


if __name__ == "__main__":
    example_for_test = MathOperations()
    assert example_for_test.get_avg_currency_rate(rates_history=[30.2, 31.6, 29.0]) == 30.3

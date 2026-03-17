"""Нужно сделать логику функции is_recovery_code_correct и аннотации в ней так, чтобы прошёл тест."""
import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Password:
    """Класс для отработки материала по @dataclasses."""

    @staticmethod
    def is_recovery_code_correct(code: str, user_codes: list[str]) -> bool:
        """Метод для проверки верности кода восстановления."""
        if code in user_codes:
            return True

        return False


if __name__ == "__main__":
    example_for_test = Password()
    assert example_for_test.is_recovery_code_correct(code="5212", user_codes=["1862", "8172", "7212"]) is False

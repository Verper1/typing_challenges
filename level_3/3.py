import dataclasses
from random import randint
from typing import Callable
from loguru import logger


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class User:
    user_id = randint(1, 1000)
    user_name: str
    user_age: int


def create_user(user_name: str, user_age: int, after_created: Callable[[int], None]) -> None:
    created_user = User(user_name=user_name, user_age=user_age)
    logger.info(f'Пользователь {created_user} был создан.')
    after_created(created_user.user_id)


def send_test_email(user_id: int) -> None:
    # Мощная логика отправления письма для подтверждения входа.
    logger.info(f"Письмо отправлено пользователю с id: {user_id}.")


if __name__ == "__main__":
    assert create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) is None

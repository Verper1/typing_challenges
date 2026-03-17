"""Нужно сделать логику функции get_current_user и аннотации в ней так, чтобы прошёл тест."""
import dataclasses
# from json import dumps


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class User:
    """dataclass хранящий в себе имя, возраст и почту пользователя."""
    name: str
    age: int
    mail: str


class UserMethods:
    """Класс для методов, которые направлены на работу с объектом класса User."""
    @staticmethod
    def get_current_user(user: User) -> tuple:
        """Возвращает кортеж с именем, возрастом и почтой объекта класса User."""
        return tuple([user.name, user.age, user.mail])

    # @staticmethod
    # def get_current_user(user: User) -> str:  # Обычно же так всегда отдаётся(((
    #     return dumps(user.__dict__, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    user_1 = User(name="Ilya Lebedev", age=33, mail="melevir@gmail.com")
    assert UserMethods.get_current_user(user_1) == ("Ilya Lebedev", 33, "melevir@gmail.com")

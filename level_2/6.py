"""Нужно сделать логику функции is_name_male и аннотации в ней так, чтобы прошёл тест."""
def is_name_male(name: str, name_gender_map: dict[str, bool]) -> bool | None:
    """Возвращает значения типа bool, если находит в словаре имя или None, если имя не в словаре."""
    return name_gender_map.get(name, None)


if __name__ == "__main__":
    name_gender_map = {
        "John": True,
        "Jane": False,
    }
    assert is_name_male("John", name_gender_map) is True
    assert is_name_male("Unknown", name_gender_map) is None

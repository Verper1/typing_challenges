"""Нужно сделать логику функции ban_users и аннотации в ней так, чтобы прошёл тест."""
banned_users = {167, 623}

def ban_users(users_ids: set[int]) -> int:
    """Функция, которая возвращает кол-во забаненных пользователей из множества."""
    response = len([True for i in users_ids if i in banned_users])
    return response

if __name__ == "__main__":
    assert ban_users(users_ids={167, 623, 209, 921}) == 2

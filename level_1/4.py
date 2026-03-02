from datetime import date, datetime

def calculate_age(date_of_birth: date) -> int:
    age = datetime.now().year - date_of_birth.year - (
            (datetime.now().month, datetime.now().day) < (date_of_birth.month, date_of_birth.day)
    )
    return age


if __name__ == "__main__":
    assert calculate_age(date_of_birth=date(1965, 6, 2)) == 60

    # UPD: Ошибку увидели и тест исправили. Было захардкожено на 2022 год как будто сейчас

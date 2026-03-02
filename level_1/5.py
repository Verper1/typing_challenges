def is_correct_email(raw_email: str) -> bool:
    sliced_str = raw_email.split("@")[1].split(".")
    response = sliced_str[1] in ["com", "ru", ...]
    return response


if __name__ == "__main__":
    assert is_correct_email(raw_email="test@gmail.co") is False
    assert is_correct_email(raw_email="test@gmail.com") is True

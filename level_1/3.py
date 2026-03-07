def compose_full_name(first_name: str, last_name: str, middle_name: str | None) -> str:
    response = f"{last_name} {first_name} {middle_name if middle_name else ""}".rstrip()
    return response


if __name__ == "__main__":
    assert compose_full_name(first_name="John", last_name="Doe", middle_name=None) == "Doe John"
    assert compose_full_name(first_name="Ilya", last_name="Lebedev", middle_name="Alexeyevich") == "Lebedev Ilya Alexeyevich"

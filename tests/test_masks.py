from src.masks import get_mask_account, get_mask_card_number


# Тестируем, что функция правильно возвращает маску карты
def test_get_mask_card_number(mask_card_number: str) -> None:
    assert get_mask_card_number("7000792289606361") == mask_card_number


# Проверяем, что пользователь ввел номер карты из 16 цифр и без лишних букв
def test_right_card_number(right_card_number: str) -> None:
    assert get_mask_card_number("12345678901234567") == right_card_number
    assert get_mask_card_number("7123345523456J81") == right_card_number
    assert get_mask_card_number("") == right_card_number


# Проверяем, что функция правильно маскирует номер счета
def test_get_mask_account(mask_account: str) -> None:
    assert get_mask_account("73654108430135874305") == mask_account


# Проверяем, что пользователь правильно ввел номер счета из 20 цифр и без лишних символов
def test_right_mask_account(right_account: str) -> None:
    assert get_mask_account("7365410843013587430") == right_account
    assert get_mask_account("736541084g0135874305") == right_account
    assert get_mask_account("") == right_account

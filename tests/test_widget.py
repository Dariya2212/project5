import pytest

from src.widget import get_date, mask_account_card


# Тестируем, что функция правильно маскирует данные счета
def test_mask_account_card(masked_account_info: str) -> None:
    assert mask_account_card("Счет 73654108430135874305") == masked_account_info


# Тестируем, что функция правильно маскирует данные карты
@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_card_info(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


# Тестируем, что данные карты или счета введены корректно
def test_right_card_info(right_account_info: str) -> None:
    assert mask_account_card("") == right_account_info
    assert mask_account_card("7000792289606361") == right_account_info
    assert mask_account_card("Visa Platinum") == right_account_info


# Тестируем, что данные даты выводятся корректно
@pytest.mark.parametrize(
    "value, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11", "11.03.2024")]
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected


# Тест с пустой датой
def test_no_date(no_date: str) -> None:
    assert get_date("") == no_date

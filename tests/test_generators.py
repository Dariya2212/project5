from typing import Dict, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


# Тестируем корректность вывода транзакций по валюте USD, и,
# если количество запрашиваемых операций больше, чем есть, с заданной валютой
def test_filter_by_currency(transactions: List[Dict]) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    for i in range(3):
        try:
            transaction = next(usd_transactions)
            print(transaction)
        except StopIteration:
            print("С указанной валютой транзакций больше нет.")
            break


# Тестируем корректность вывода транзакций при указании другой валюты
def test_filter_by_different_currency(dif_transactions: List[Dict]) -> None:
    usd_transactions = filter_by_currency(dif_transactions, "RU")
    for i in range(1):
        try:
            transaction = next(usd_transactions)
            print(transaction)
        except StopIteration:
            print("С указанной валютой транзакций больше нет.")
            break


# Тестируем корректность вывода транзакций при указании отсутствующей валюты
def test_filter_by_unknown_currency(dif_transactions: List[Dict]) -> None:
    usd_transactions = filter_by_currency(dif_transactions, "EUR")
    for i in range(2):
        try:
            transaction = next(usd_transactions)
            print(transaction)
        except StopIteration:
            print("С указанной валютой транзакций нет.")
            break


# Тестируем корректность вывода описания для каждой транзакции
def test_transaction_descriptions(transactions: List[Dict]) -> None:
    description = transaction_descriptions(transactions)
    for i in range(5):
        try:
            print(next(description))
        except StopIteration:
            print("Транзакций больше нет.")
            break


# Тестируем работу функции при отсутстыии параметра descriprion
# или при наличии пустого списка
def test_empty_transaction_descriptions(transactions_empty_description: List[Dict]) -> None:
    description = transaction_descriptions(transactions_empty_description)
    for i in range(5):
        try:
            print(next(description))
        except StopIteration:
            print("Транзакций больше нет.")
            break


# Тестируем корректность вывода номеров карт в разных диапазонах
@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected_numbers: str) -> None:
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected_numbers


# Тестируем корректность вывода номеров карт в указанном диапазоне
def test_card_number_generator_2() -> None:
    for card_number in card_number_generator(1, 5):
        print(card_number)


# Тестируем корректность работы функции, если диапазон неверный - от большего к меньшему
def test_empty_range() -> None:
    for card_number in card_number_generator(9, 3):
        print(card_number)


# Тестируем корректность работы функции, если диапазон отрицательный
def test_negative_range() -> None:
    for card_number in card_number_generator(-4, -1):
        print(card_number)


# Тестируем корректность работы функции при большом диапазоне
def test_big_range() -> None:
    for card_number in card_number_generator(1, 99):
        print(card_number)

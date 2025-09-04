from typing import Dict, List

from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)


# Тестируем фильтрацию списка словарей по статусу EXECUTED
def test_filter_by_executed(bank_data: List[Dict]) -> None:
    assert filter_by_state(bank_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Тестируем фильтрацию списка словарей по статусу CANSELED
def test_filter_by_canseled(bank_data: List[Dict]) -> None:
    assert filter_by_state(bank_data, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Тестируем фильтрацию списка словарей, если в некоторых соварях отсутствует параметр state
def test_filter_by_none(bank_data_state_none: List[Dict]) -> None:
    assert filter_by_state(bank_data_state_none) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Тестируем сортировку списка словарей по датам в порядке убывания
def test_sort_in_ascending_order(bank_data: List[Dict]) -> None:
    assert sort_by_date(bank_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Тестируем сортировку списка словарей по датам в порядке возрастания
def test_sort_in_descending_order(bank_data: List[Dict]) -> None:
    assert sort_by_date(bank_data, sorting_type=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Тест сортировки списка словарей при наличии одинаковых дат
def test_sort_same_dates(same_dates: List[Dict], sorted_same_dates: List[Dict]) -> None:
    assert sort_by_date(same_dates) == sorted_same_dates


# Тест на корректность работы функции (в т.ч. с разным регистром) и правильного подсчета количества
data = [
    {"description": "Оплата коммунальных услуг"},
    {"description": "Покупка в магазине"},
    {"description": "Перевод на карту"},
    {"description": "оплата коммунальных услуг"},
    {"description": "Покупка стройматериалов"},
    {"description": "Перевод на карту"},
]

categories = ["оплата коммунальных услуг", "покупка", "перевод"]


def test_process_bank_operations():
    result = process_bank_operations(data, categories)
    expected = {
        "оплата коммунальных услуг": 2,
        "покупка": 2,
        "перевод": 2,
    }
    assert result == expected, f"Тест не прошел: {result} != {expected}"
    print("Все тесты прошли успешно.")


test_process_bank_operations()


def test_process_bank_search(data_for_processing):
    # поиск слова "перевод"
    result = process_bank_search(data_for_processing, "перевод")
    assert len(result) == 2
    assert all("перевод" in item.get("description", "").lower() for item in result)

    # поиск слова, которого нет
    result = process_bank_search(data_for_processing, "займ")
    assert result == []

    # поиск пустой строки (должен вернуть все элементы)
    result = process_bank_search(data_for_processing, "")
    assert len(result) == len(data_for_processing)

    # поиск с разным регистром
    result1 = process_bank_search(data_for_processing, "ПЕРЕВОД")
    result2 = process_bank_search(data_for_processing, "перевод")
    assert result1 == result2

    # элементы без описания не вызывают ошибку и не попадают в результат, если не совпадают
    result = process_bank_search(data_for_processing, "покупка")
    assert len(result) == 1
    assert result[0].get("description") == "Покупка продуктов"


def test_process_bank_operations(data_for_processing_1):
    categories = ["Перевод", "Оплата", "Покупка"]
    result = process_bank_operations(data_for_processing_1, categories)

    # Проверяем, что подсчёт корректен
    assert result.get("Перевод") == 3, f"Expected 3, got {result.get('Перевод')}"
    assert result.get("Оплата") == 2, f"Expected 2, got {result.get('Оплата')}"
    assert result.get("Покупка") == 1, f"Expected 1, got {result.get('Покупка')}"

    # Категории, которые не встречаются, не должны быть в словаре
    assert "Вклад" not in result

    # Проверяем, что пустые описания не влияют на результат
    assert sum(result.values()) == 6

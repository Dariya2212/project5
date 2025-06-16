from typing import Dict, List

from src.processing import filter_by_state, sort_by_date


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

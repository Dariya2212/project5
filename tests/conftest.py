from typing import Dict, List

import pytest


@pytest.fixture
def mask_card_number() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def right_card_number() -> str:
    return "Номер карты должен состоять из 16 цифр"


@pytest.fixture
def mask_account() -> str:
    return "**4305"


@pytest.fixture
def right_account() -> str:
    return "Номер счета должен состоять из 20 цифр"


@pytest.fixture
def masked_account_info() -> str:
    return "Счет **4305"


@pytest.fixture
def right_account_info() -> str:
    return "Введите корректные данные карты или счета"


@pytest.fixture
def no_date() -> str:
    return "Дата не определена"


@pytest.fixture
def bank_data() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def bank_data_state_none() -> List[Dict]:
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def same_dates() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_same_dates() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


# @pytest.fixture
# def missing_date():
#     return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#             {'id': 939719570, 'state': 'EXECUTED'},
#             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#             ]


# @pytest.fixture
# def sorted_missing_date():
#     return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#             ]

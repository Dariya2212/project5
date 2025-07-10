from unittest.mock import mock_open, patch

import pandas as pd

from financial_operations import (
    read_financial_operations_csv,
    read_financial_operations_excel,
)


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date\n650703;EXECUTED;2023-09-05T11:30:32Z\n3598919;EXECUTED;2020-12-06T23:00:58Z",
)
def test_read_financial_operations_csv(mock_open):

    # Тестируем вызов функции
    result = read_financial_operations_csv("fake_path.csv")

    # Тестируем, что open вызван с правильным путём
    mock_open.assert_called_once_with("fake_path.csv", encoding="utf-8")

    # Тестируем, что выводится список словарей
    expected = [
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"},
        {"id": "3598919", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_read_financial_operations_excel(mock_read_excel):
    # Создаём DataFrame, который вернёт мок
    mock_df = pd.DataFrame(
        [
            {"id": 650703, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": 16210},
            {"id": 3598919, "state": "EXECUTED", "date": "2020-12-06T23:00:58Z", "amount": 29740},
        ]
    )
    mock_read_excel.return_value = mock_df

    # Тестируем вызов функции
    result = read_financial_operations_excel("fake_path.xlsx")

    # Проверка, что pd.read_excel вызван с правильным путём
    mock_read_excel.assert_called_once_with("fake_path.xlsx")

    # Тестируем, что выводится список словарей
    expected = [
        {"id": 650703, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": 16210},
        {"id": 3598919, "state": "EXECUTED", "date": "2020-12-06T23:00:58Z", "amount": 29740},
    ]
    assert result == expected

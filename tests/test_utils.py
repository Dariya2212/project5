import json
from unittest.mock import mock_open, patch

from src.processing import process_bank_search
from src.utils import load_transactions


def test_load_transactions(test_operations):
    """
    Тестируем корректность преобразования данных JSON-файла в список
    """

    json_data = json.dumps(test_operations)
    with patch("builtins.open", mock_open(read_data=json_data)):
        result = load_transactions("fake_path.json")
    assert result == test_operations


def test_empty_load_transactions():
    """
    Тестируем, что функция при отсутствии данных, возвращает пустой список
    """

    json_data = json.dumps([])
    with patch("builtins.open", mock_open(read_data=json_data)):
        result = load_transactions("fake_path.json")
    assert result == []

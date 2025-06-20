from unittest.mock import Mock, patch

import requests

from src.external_api import get_exchange_rate


def test_get_exchange_rate_success():
    """
    Тестируем получение курса валюты USD
    """
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"rates": {"USD": 70.5}}

    with patch("requests.get", return_value=mock_response):
        rate = get_exchange_rate("USD")
        assert rate == 70.5


def test_get_exchange_rate():
    """
    Тестируем получение курса валюты EUR
    """
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"rates": {"EUR": 101.4}}

    with patch("requests.get", return_value=mock_response):
        rate = get_exchange_rate("EUR")
        assert rate == 101.4


def test_get_exchange_rate_http_error():
    """
    Тест обработки ошибки HTTPError
    """

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

    with patch("requests.get", return_value=mock_response):
        result = get_exchange_rate("USD")
        assert result == "HTTP Error. Please check the URL."


def test_get_exchange_rate_key_error():
    """
    Тест обработки ошибки KeyError
    """

    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"rates": {}}

    with patch("requests.get", return_value=mock_response):
        result = get_exchange_rate("USD")
        assert result == "Key not found."


def test_get_exchange_rate_value_error():
    """
    Тест обработки ошибки ValueError
    """

    mock_response = Mock()
    mock_response.raise_for_status = Mock()

    def json_side_effect():
        raise ValueError()

    mock_response.json.side_effect = json_side_effect

    with patch("requests.get", return_value=mock_response):
        result = get_exchange_rate("USD")
        assert result == "Value USD not found."

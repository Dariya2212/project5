import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
url = "https://apilayer.com/exchangerates_data-api"


def get_exchange_rate(currency):
    """
    Получает текущий курс обмена для валюты currency к рублю.
    Возвращает курс как float.
    """

    try:
        headers = {"apikey": API_KEY}
        params = {"base": "RUB", "symbols": currency}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        return data["rates"][currency]
    except requests.exceptions.HTTPError:
        return "HTTP Error. Please check the URL."
    except TypeError:
        return "Object of type is non JSON serializable."
    except KeyError:
        return "Key not found."
    except ValueError:
        return f"Value {currency} not found."


def convert_to_rub(amount, currency):
    """
    Конвертирует сумму из валюты EUR или USD в рубли.
    """

    try:
        if currency == "RUB":
            return float(amount)
        elif currency in ["USD", "EUR"]:
            rate = get_exchange_rate(currency)
            return float(amount) * rate
        else:
            raise ValueError("Поддерживаются только валюты USD, EUR и RUB")
    except requests.exceptions.RequestException:
        print("Ошибка при конвертации данных.")

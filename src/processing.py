import re
from collections import Counter
from typing import Dict, List


def filter_by_state(bank_data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
    возвращает новый список, содержащий только те словари, у которых ключ state содержит
    переданное в функцию значение.
    """

    filtered_bank_data: List[Dict] = []
    state = state.strip().upper()
    for i in bank_data:
        if i.get("state") == state:
            filtered_bank_data.append(i)
    return filtered_bank_data


def sort_by_date(bank_data: List[Dict], sorting_type: bool = True) -> List[Dict]:
    """
    Функция принимает список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате
    """

    sorted_bank_data: List[Dict] = sorted(bank_data, key=lambda x: x["date"], reverse=sorting_type)
    return sorted_bank_data


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = []
    for item in data:
        description = item.get("description", "")
        if pattern.search(description):
            result.append(item)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    pattern_dict = {}
    for category in categories:
        pattern = re.compile(r"\b" + re.escape(category) + r"\b", re.IGNORECASE)
        pattern_dict[category] = pattern

    # Подсчет кол-ва операций
    counter_operations = Counter()

    for operation in data:
        description = operation.get("description", "")
        for category, pattern in pattern_dict.items():
            if pattern.search(description):
                counter_operations[category] += 1
                break

    return dict(counter_operations)

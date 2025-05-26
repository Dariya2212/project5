from typing import Dict, List


def filter_by_state(bank_data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
    возвращает новый список, содержащий только те словари, у которых ключ state содержит
    переданное в функцию значение.
    """

    filtered_bank_data: List[Dict] = []
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

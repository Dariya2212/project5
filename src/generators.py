from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency_code: object = "USD") -> Generator[dict, Any, None]:
    """
    Функция принимает на вход список словарей, представляющих транзакции
    и возвращает итератор, который поочередно выдает транзакции
    """
    for transaction in transactions:
        if transaction is None:
            print("Транзакций больше нет.")
        elif (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "code" in transaction["operationAmount"]["currency"]
        ):
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str | None | Any, Any, None]:
    """
    Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]
        else:
            yield ""


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    """

    for number in range(start, end + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_num = f"{number:016d}"

        # Разбиваем на группы по 4 цифры
        formatted_card_number = " ".join([card_num[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number

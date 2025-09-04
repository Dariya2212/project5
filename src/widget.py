from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""

    if card_info == "":
        return "Введите корректные данные карты или счета"
    parts = card_info.split(" ")
    card_number = parts[-1]
    card_type = " ".join(parts[:-1])
    for i in card_number:
        if i.isalpha():
            return "Введите корректные данные карты или счета"
    if card_type == "Счет":
        masked_number = get_mask_account(card_number)
        return f"{card_type} {masked_number}"
    elif card_type == "":
        return "Введите корректные данные карты или счета"
    else:
        masked_number = get_mask_card_number(card_number)
        return f"{card_type} {masked_number}"


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в длинном формате и возвращает короткий вариант даты"""

    if date == "":
        return "Дата не определена"
    else:
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        return f"{day}.{month}.{year}"


def format_transaction(transaction):
    """
    Функция преобразует отформатированный и отсортированный словарь транзакций в вывод вида:
        дата, вид транзакции
        Счет
        Сумма
    """

    date_str = get_date(transaction.get("date", ""))
    description = transaction.get("description", "").strip()

    # Попытка получить сумму и валюту из вложенного словаря
    if "operationAmount" in transaction:
        amount_info = transaction.get("operationAmount", {})
        amount = amount_info.get("amount", "")
        currency_code = amount_info.get("currency", {}).get("code", "")
    else:
        # Для Excel/CSV - поля на верхнем уровне
        amount = transaction.get("amount", "")
        currency_code = transaction.get("currency_code", "")

    sum_str = f"{amount} {currency_code}"

    # Попытка получить from и to
    from_info = transaction.get("from", "") or transaction.get("from_account", "") or ""
    to_info = transaction.get("to", "") or transaction.get("to_account", "") or ""

    from_str = mask_account_card(str(from_info)) if from_info else ""
    to_str = mask_account_card(str(to_info)) if to_info else ""

    if from_str and to_str:
        line1 = f"{date_str} {description}"
        line2 = f"{from_str} -> {to_str}"
        line3 = f"Сумма: {sum_str}"
        return f"{line1}\n{line2}\n{line3}"
    elif from_str:
        line1 = f"{date_str} {description}"
        line2 = from_str
        line3 = f"Сумма: {sum_str}"
        return f"{line1}\n{line2}\n{line3}"
    elif to_str:
        line1 = f"{date_str} {description}"
        line2 = to_str
        line3 = f"Сумма: {sum_str}"
        return f"{line1}\n{line2}\n{line3}"
    else:
        line1 = f"{date_str} {description}"
        line2 = f"Сумма: {sum_str}"
        return f"{line1}\n{line2}"

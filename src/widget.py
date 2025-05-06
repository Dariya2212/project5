from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""

    parts = card_info.split(" ")
    card_number = parts[-1]
    card_type = " ".join(parts[:-1])
    if card_type == "Счет":
        masked_number = get_mask_account(card_number)
        return f"{card_type} {masked_number}"
    else:
        masked_number = get_mask_card_number(card_number)
        return f"{card_type} {masked_number}"


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в длинном формате и возвращает короткий вариант даты"""

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}.{month}.{year}"

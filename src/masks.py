def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    for i in card_number:
        if i.isalpha():
            return "Номер карты должен состоять из 16 цифр"
    if len(card_number) != 16:
        return "Номер карты должен состоять из 16 цифр"
    else:
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    for i in account_number:
        if i.isalpha():
            return "Номер счета должен состоять из 20 цифр"
    if len(account_number) != 20:
        return "Номер счета должен состоять из 20 цифр"
    else:
        masked_account_number = f"**{account_number[-4:]}"
        return masked_account_number

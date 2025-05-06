def get_mask_card_number(card_number):
    """Функция принимает на вход номер карты и возвращает ее маску"""

    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card_number


card_number = ""
masked_number = get_mask_card_number(card_number)
print(masked_number)


def get_mask_account(account_number):
    """Функция принимает на вход номер счета и возвращает его маску"""

    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number


account_number = ""
masked_account = get_mask_account(account_number)
print(masked_account)

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


def mask_account_card(
    card_info: str,
) -> str:
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


card_info = "Счет 64686473678894779589"
masked_number = mask_account_card(card_info)
print(masked_number)


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в длинном формате и возвращает короткий вариант даты"""

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}.{month}.{year}"


date = "2024-03-11T02:26:18.671407"
print(get_date(date))


def filter_by_state(bank_data: [dict], state="EXECUTED") -> [dict]:
    '''Функция принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение.'''

    filtered_bank_data = []
    for i in bank_data:
        if i.get("state") == state:
            filtered_bank_data.append(i)
    return filtered_bank_data


bank_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(bank_data))
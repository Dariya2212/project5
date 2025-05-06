from src.masks import get_mask_account, get_mask_card_number

card_number = ""
masked_card = get_mask_card_number(card_number)
print(masked_card)


account_number = ""
masked_account = get_mask_account(account_number)
print(masked_account)

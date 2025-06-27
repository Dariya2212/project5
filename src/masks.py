import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Projects/PythonProject5/logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    try:
        for i in card_number:
            if i.isalpha():
                logger.error("Введен номер карты, состоящий не из 16 цифр.")
                return "Номер карты должен состоять из 16 цифр"
        if len(card_number) != 16:
            logger.error("Введен номер карты, состоящий не из 16 цифр.")
            return "Номер карты должен состоять из 16 цифр"
        else:
            masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            logger.info("Введен корректный номер карты.")
            return masked_card_number
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}.")


def get_mask_account(account_number: str) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску"""

    try:
        for i in account_number:
            if i.isalpha():
                logger.error("Введен некорректный номер счета.")
                return "Номер счета должен состоять из 20 цифр"
        if len(account_number) != 20:
            logger.error("Введен некорректный номер счета.")
            return "Номер счета должен состоять из 20 цифр"
        else:
            logger.info("Введен корректный номер счета.")
            masked_account_number = f"**{account_number[-4:]}"
            return masked_account_number
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}.")

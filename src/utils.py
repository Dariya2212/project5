import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Projects/PythonProject5/logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(json_path):
    """
    Функция преобразует данные JSON-файла в список
    """

    try:
        logger.info("Преобразуем данные JSON-файла в список")
        with open(json_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
    except (json.JSONDecodeError, TypeError, KeyError, ValueError):
        logger.error("Произошла ошибка.")
        return []
    except FileNotFoundError:
        logger.error("Файл не найден.")
        return []
    return operations

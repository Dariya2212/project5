import re

from financial_operations import (
    read_financial_operations_csv,
    read_financial_operations_excel,
)
from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)
from src.utils import load_transactions
from src.widget import format_transaction

PATH_TO_JSON = "C:/Projects/PythonProject5/data/operations.json"
PATH_TO_CSV = "C:/Projects/PythonProject5/data/transactions.csv"
PATH_TO_XLSX = "C:/Projects/PythonProject5/data/transactions_excel.xlsx"  # добавил расширение


def main():
    """
    Функция предоставляет пользовательский интерфейс и связывает все функциональности между собой
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        try:
            print("Выберите необходимый пункт меню:")
            print(
                """
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
            )
            choice_1 = int(input("Пользователь: ").strip())

            if choice_1 == 1:
                print("Для обработки выбран JSON-файл")
                transactions = load_transactions(PATH_TO_JSON)
                break  # выход из цикла после успешного выбора

            elif choice_1 == 2:
                print("Для обработки выбран CSV-файл")
                transactions = read_financial_operations_csv(PATH_TO_CSV)
                break

            elif choice_1 == 3:
                print("Для обработки выбран XLSX-файл")
                transactions = read_financial_operations_excel(PATH_TO_XLSX)
                break
        except ValueError:
            print("\nПожалуйста, введите число от 1 до 3.")

    while True:
        try:
            print(
                """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
            )

            choice_2 = input("\nПользователь: ").upper()

            if choice_2 == "EXECUTED":
                print("\nОперации отфильтрованы по статусу EXECUTED")
                transactions_1 = filter_by_state(transactions, state="EXECUTED")
                break

            elif choice_2 == "CANCELED":
                print("\nОперации отфильтрованы по статусу CANCELED")
                transactions_1 = filter_by_state(transactions, state="CANCELED")
                break

            elif choice_2 == "PENDING":
                print("\nОперации отфильтрованы по статусу PENDING")
                transactions_1 = filter_by_state(transactions, state="PENDING")
                break

            else:
                print(f"\nСтатус операции {choice_2} недоступен.")

        except ValueError:
            print(f"\nСтатус операции {choice_2} недоступен.")

    while True:
        try:
            print("\nОтсортировать операции по дате? Да/Нет")
            choice_3 = input().lower()

            if choice_3 == "да":
                print("\nОтсортировать операции по возрастанию или по убыванию? по возрастанию/по убыванию")
                choice_4 = input().lower()
                if choice_4 == "по убыванию":
                    transactions_2 = sort_by_date(transactions_1)
                elif choice_4 == "по возрастанию":
                    transactions_2 = sort_by_date(transactions_1, sorting_type=False)
                else:
                    print("\nНекорректный ввод для сортировки. Попробуйте снова.")
                    continue
                break
            elif choice_3 == "нет":
                transactions_2 = transactions_1
                break
            else:
                print("\nПожалуйста, введите 'Да' или 'Нет'.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break

    def is_rub(transaction):
        if "operationAmount" in transaction:
            code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "").strip().upper()
            return code == "RUB"
        else:
            code = transaction.get("currency_code", "").strip().upper()
            return code == "RUB"

    while True:
        try:
            print("\nВыводить только рублевые транзакции? Да/Нет")
            choice_5 = input().lower()

            if choice_5 == "да":
                transactions_3 = [t for t in transactions_2 if is_rub(t)]
                break
            elif choice_5 == "нет":
                transactions_3 = transactions_2
                break
            else:
                print("\nПожалуйста, введите 'Да' или 'Нет'.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break

    while True:
        try:
            print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
            choice_6 = input().lower()

            if choice_6 == "да":
                print("\nВведите слово для сортировки: ")
                word_to_sort = input()
                if any(
                    re.search(re.escape(word_to_sort), item.get("description", ""), re.IGNORECASE)
                    for item in transactions_3
                ):
                    transactions_4 = process_bank_search(transactions_3, search=word_to_sort)
                else:
                    print(f'\nСлово "{word_to_sort}" не найдено, сортировка по нему невозможна.')
                    continue
                break
            elif choice_6 == "нет":
                transactions_4 = transactions_3
                break
            else:
                print("\nПожалуйста, введите 'Да' или 'Нет'.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break

    categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]
    print(f"\nВсего банковских операций в выборке: {len(transactions_4)}")
    if len(transactions_4) > 0:
        stats = process_bank_operations(transactions_4, categories)
        print("\nСтатистика по категориям операций:")
        for category, count in stats.items():
            print(f"{category}: {count}")

        result = "\n\n".join(format_transaction(t) for t in transactions_4)
        return result
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


print(main())

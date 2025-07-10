import csv

import pandas as pd


def read_financial_operations_csv(csv_path):
    """
    Функция, считывающая данные о финансовых операциях из csv-файла, и возвращающая список словарей
    """

    csv_transaction_data = []
    with open(csv_path, encoding="utf-8") as transactions_csv:
        reader = csv.DictReader(transactions_csv, delimiter=";")
        for row in reader:
            csv_transaction_data.append(row)
    return csv_transaction_data


transactions_csv_list = read_financial_operations_csv("C:\\Projects\\PythonProject5\\data\\transactions.csv")


def read_financial_operations_excel(excel_path):
    """
    Функция, считывающая данные о финансовых операциях из excel-файла, и возвращающая список словарей
    """

    excel_transaction_data = pd.read_excel(excel_path)
    excel_transaction_data_list = excel_transaction_data.to_dict(orient="records")
    return excel_transaction_data_list


transactions_excel_list = read_financial_operations_excel(
    "C:\\Projects\\PythonProject5\\data\\transactions_excel.xlsx"
)

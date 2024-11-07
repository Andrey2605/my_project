import pandas as pd
from typing import Any

def get_transactions_excel(transaction_excel: str)->list:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями."""
    try:
        transactions_excel = pd.read_excel(transaction_excel)
        transact_excel = transactions_excel.to_dict(orient="records")
        return transact_excel
    except FileNotFoundError:
        return []


def get_transactions_csv(transactions_csv: Any)->Any:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    try:
        transactions_csv = pd.read_csv(transactions_csv, sep=";", decimal=",", encoding="utf-8")
        transact_csv = transactions_csv.to_dict(orient="records")
        return transact_csv
    except FileNotFoundError:
        return []

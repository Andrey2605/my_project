import pandas as pd


def get_transactions_excel(transaction_excel):
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями."""
    try:
        transactions_excel = pd.read_excel(transaction_excel)
        transact_excel = transactions_excel.to_dict(orient="records")
        return transact_excel
    except FileNotFoundError:
        return []


def get_transaction_csv(transaction_csv):
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    try:
        transaction_csv = pd.read_csv(transaction_csv)
        transact_csv = transaction_csv.to_dict(orient="records")
        return transact_csv
    except FileNotFoundError:
        return []

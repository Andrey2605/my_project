import pandas as pd


def get_transactions_excel():
    '''Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями.'''
    try:
        transactions_excel = pd.read_excel("../data/transactions_excel.xlsx")
        return transactions_excel
    except FileNotFoundError:
        return []


def get_transaction_csv():
    '''Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями'''
    try:
        transaction_csv = pd.read_csv("../data/transactions.csv")
        return transaction_csv
    except FileNotFoundError:
        return []

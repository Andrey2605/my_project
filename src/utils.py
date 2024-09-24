import json
from typing import Any

from src.external_api import currency_conversion


def read_file(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="UTF8") as file_json:
            json_file = json.load(file_json)
            return json_file
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


def transaction_amount(transaction: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
    else:
        amount = currency_conversion(transaction)
    return amount

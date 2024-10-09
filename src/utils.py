import json
import logging
from typing import Any

from src.external_api import currency_conversion

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_file(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info("Выполняем открытие файла JSON")
        with open(path, encoding="UTF8") as file_json:
            json_file = json.load(file_json)
            return json_file
    except json.JSONDecodeError as e:
        logger.error(f"Произошла ошибка: {e}")
        return []
    except FileNotFoundError as e:
        logger.error(f"Произошла ошибка: {e}")
        return []


def transaction_amount(transaction: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    logger.info("Выполняем проверку валюты")
    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
    else:
        amount = currency_conversion(transaction)
    return amount

import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")

headers = {"apikey": apikey}


def currency_conversion(transaction: dict) -> Any:
    """Функция конвертации"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.get(url, headers=headers)
    result = response.json()
    return result["result"]

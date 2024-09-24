from typing import Any
from unittest.mock import patch

from src.external_api import currency_conversion


@patch("requests.get")
def test_currency_conversion(mock_get: Any, transaction_usd: dict) -> Any:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1726858564, "rate": 92.34757},
        "date": "2024-09-20",
        "result": 759223.541571,
    }

    assert currency_conversion(transaction_usd) == 759223.541571

import json
from typing import Any

from src.utils import read_file, transaction_amount


def test_open_file_json(path: str) -> Any:
    with open(path, encoding="UTF8") as file_json:
        json_file = json.load(file_json)
    assert read_file(path) == json_file


def test_open_file_json_error(json_error: str) -> Any:
    with open(json_error, encoding="UTF8") as file_json:
        json_file = json.load(file_json)
    assert read_file(json_error) == json_file


def test_transaction_amount(transaction: dict) -> Any:
    assert transaction_amount(transaction) == "31957.58"

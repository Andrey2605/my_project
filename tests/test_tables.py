from unittest.mock import patch

from pandas import DataFrame

from src.tables import get_transaction_csv, get_transactions_excel


@patch("pandas.read_excel")
def test_get_transactions_excel(mock_read_excel):
    mock_read_excel.return_value = DataFrame({"key": ["value"]})
    assert get_transactions_excel("test_file") == [{"key": "value"}]


@patch("pandas.read_csv")
def test_get_transaction_csv(mock_read_csv):
    mock_read_csv.return_value = DataFrame({"key": ["value"]})
    assert get_transaction_csv("test_file") == [{"key": "value"}]

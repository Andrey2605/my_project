from unittest.mock import patch

from src.tables import get_transaction_csv, get_transactions_excel


@patch("src.tables.pd.read_excel")
def test_get_transactions_excel(mock):
    mock.return_value = []
    assert get_transactions_excel() == []


@patch("src.tables.pd.read_csv")
def test_get_transaction_csv(mock):
    mock.return_value = []
    assert get_transaction_csv() == []

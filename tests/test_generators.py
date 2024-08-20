import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency() -> None:
    """Тест проверяющий, что функция корректно фильтрует транзакции по заданной валюте."""
    assert next(filter_by_currency(transactions, currency="USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_zero() -> None:
    """Тест, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций."""
    with pytest.raises(ValueError) as exc_info:
        next(filter_by_currency(transactions, currency="0"))
    assert str(exc_info.value) == "Не коррекные данные"
    with pytest.raises(ValueError) as exc_info:
        next(filter_by_currency(transactions, currency=" "))
    assert str(exc_info.value) == "Не коррекные данные"


def test_filter_by_currency_eu() -> None:
    """Тест, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют."""
    with pytest.raises(ValueError) as exc_info:
        next(filter_by_currency(transactions, currency="eu"))
    assert str(exc_info.value) == "Не коррекные данные"


def test_transaction_descriptions(translition: str) -> None:
    """Тест, что функция возвращает корректные описания для каждой транзакции."""
    assert next(transaction_descriptions(transactions)) == translition


def test_transaction_descriptions_zero() -> None:
    """Тест функции с пустым списоком."""
    with pytest.raises(ValueError) as exc_info:
        next(transaction_descriptions([]))
    assert str(exc_info.value) == "Не коррекные данные"


def test_card_number_generator() -> None:
    """Тесты, который проверяет, что генератор выдает правильные номера карт в заданном диапазоне."""
    assert next(card_number_generator(10, 11)) == "0000 0000 0000 0010"


def test_card_number_generator_first() -> None:
    """Тест, что генератор корректно обрабатывает крайние значения диапазона."""
    assert next(card_number_generator(0, 1)) == "0000 0000 0000 0000"


def test_card_number_generator_end() -> None:
    """Тест, что генератор правильно завершает генерацию."""
    assert next(card_number_generator(9999999999999998, 9999999999999999)) == "9999 9999 9999 9998"

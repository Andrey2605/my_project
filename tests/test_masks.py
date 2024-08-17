import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, mask_number",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(number_card, mask_number):
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(number_card) == mask_number


@pytest.mark.parametrize(
    "account, mask_account",
    [("64686473678894779589", "**9589"), ("35383033474447895560", "**5560"), ("73654108430135874305", "**4305")],
)
def test_get_mask_account(account, mask_account):
    """Тестирование правильности маскирования счетов"""
    assert get_mask_account(account) == mask_account


def test_get_mask_right_card_number(incorrect_data):
    """Тестирование на првильность ввода номера карт"""
    assert get_mask_card_number("1234") == incorrect_data
    assert get_mask_card_number("hello") == incorrect_data


def test_get_mask_card_not_number(incorrect_data):
    """Тест при отстутствии номера карты"""
    assert get_mask_card_number("") == incorrect_data


def test_get_mask_right_account(incorrect_data):
    """Тестирование на првильность ввода счета"""
    assert get_mask_account("12351") == incorrect_data
    assert get_mask_account("hello!") == incorrect_data


def test_get_mask_not_account(incorrect_data):
    """Тест при отсутствии номера счета"""
    assert get_mask_account("") == incorrect_data

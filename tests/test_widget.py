import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "number, mask_account_and_card",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ]
)
def test_mask_account_card(number, mask_account_and_card):
    """Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных, а также тесты с разными типами карт и счетов для проверки универсальности функции."""
    assert mask_account_card(number) == mask_account_and_card


def test_mask_account_card_errors(incorrect_data):
    """Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам."""
    assert mask_account_card("Счет 1234") == incorrect_data
    assert mask_account_card(" Счет hello") == incorrect_data
    assert mask_account_card("Visa Platinum 12345") == incorrect_data
    assert mask_account_card("Visa Platinum hello") == incorrect_data
    assert mask_account_card("") == incorrect_data


def test_get_date():
    """Тестирование правильности преобразования даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_not_standart(incorrect_data):
    """Тестирование работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами."""
    assert get_date("2024-03-11") == incorrect_data
    assert get_date("456456464") == incorrect_data
    assert get_date("hello") == incorrect_data


def test_get_not_date(incorrect_data):
    """Тестирование, что функция корректно обрабатывает входные строки, где отсутствует дата."""
    assert get_date(" ") == incorrect_data

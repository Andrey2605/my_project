import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_state):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(filter_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state():
    """Тест при отсутствии словарей с указанным статусом state в списке."""
    assert filter_by_state(state="DEVAISE") == []


def test_filter_by_state():
    """Тест для различных возможных значений статуса state"""
    assert filter_by_state(state="1234") == []
    assert filter_by_state(state="hello") == []


def test_sort_by_date(date, sorted_list_descending):
    """Тестирование сортировки списка словарей по датам в порядке убывания"""
    assert sort_by_date(date) == sorted_list_descending


def test_sort_by_date(sorted_list_identical):
    """Тест корректности сортировки при одинаковых датах"""
    assert sort_by_date(sorted_list_identical) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date(sorted_list_not_standard):
    """Тесты на работу функции с некорректными или нестандартными форматами дат."""
    assert sort_by_date(sorted_list_not_standard) == [
        {"id": 939719570, "state": "EXECUTED", "date": ":58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": ":29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2.241689"},
    ]

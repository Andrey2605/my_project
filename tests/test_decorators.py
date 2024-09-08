import tempfile

import pytest

from src.decorators import log


def test_log_good(capsys):
    """Тестирует выполнение декорированной функции"""

    @log()
    def func(x, y):
        return x + y

    func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "func ок\n"


def test_log_good_file_log(capsys):
    """Тестирует запись в файл после успешного выполнения"""

    with open("mylog.txt", "w", encoding="utf-8") as file:
        file.write("func ок")

    @log(filename="mylog.txt")
    def func(x, y):
        return x + y

    func(1, 2)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        logs = file.read()

    assert "func ок" in logs


def test_log_exception_file_log(capsys):
    """Тестирует запись в файл после ошибки"""

    with open("mylog.txt", "w", encoding="utf-8") as file:
        file.write("func error: unsupported operand type(s) for +: 'int' and 'str' Inputs: (1, '2')")

    @log(filename="mylog.txt")
    def func(x, y):
        return x + y

    func(1, "2")

    with open("mylog.txt", "r", encoding="utf-8") as file:
        logs = file.read()

    assert ("func error: unsupported operand type(s) for +: 'int' and 'str' Inputs: (1, '2')") in logs

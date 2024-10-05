from typing import Any


def log(filename: Any = None)-> Any:
    """Декоратор для вывода функции в консоль и запись в файл"""
    def decarator(func: Any)->Any:
        def wrapper(*args: Any, **kwargs: Any)->Any:
            result = None
            try:
                result = func(*args, **kwargs)
                if filename:
                    # Выводить лог в файл
                    with open("mylog.txt", "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ок")
                else:
                    # Выводить лог в терминал
                    print(f"{func.__name__} ок")
            except Exception as e:
                if filename:
                    # Выводить лог в файл
                    with open("mylog.txt", "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e} Inputs: {args}")
                else:
                    # Выводить лог в терминал
                    print(f"{func.__name__} error: {e} Inputs: {args}")
            return result

        return wrapper

    return decarator


@log(filename="mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    return x + y


my_function(1, "2")

def log(filename=None):
    def decarator(func):
        def wrapper(*args, **kwargs):
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
def my_function(x, y):
    return x + y

my_function(1,"2" )

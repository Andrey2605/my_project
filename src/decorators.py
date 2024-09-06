def log(filename = None):
    def my_decarator(func):
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
                if filename:
                    # Выводить лог в файл
                    with open('mylog.txt', 'w') as file:
                        file.write(f"{func.name} ок")
                else:
                    # Выводить лог в терминал
                    print(f"{func.name} ок")
            except Exception as e:
                if filename:
                    # Выводить лог в файл
                    with open('mylog.txt', 'w') as e:
                        e.write(f"{func.name} error: {e} Inputs: {args}")
                else:
                    # Выводить лог в терминал
                    print(f"{func.name} error: {e} Inputs: {args}")
            return result
        return wrapper
    return my_decarator


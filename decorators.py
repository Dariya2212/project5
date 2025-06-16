from functools import wraps


def log(filename=None):
    def decorator(my_func):
        """
        Декоратор автоматически логирует начало и конец выполнения функции,
        а также ее результаты или возникшие ошибки
        """

        @wraps(my_func)
        def wrapper(*args, **kwargs):
            func_name = my_func.__name__
            try:
                result = my_func(*args, **kwargs)
            except Exception as e:
                # Обработка ошибки
                error_type = type(e).__name__
                message = f"{func_name} error: {error_type}. Inputs: {args}, {kwargs}"
                # Запись ошибки в лог
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                print(message)
                raise
                # Успешное выполнение
            else:
                message = f"{func_name} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                print(message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


# my_function(1.8, 2)

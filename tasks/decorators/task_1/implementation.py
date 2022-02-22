import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        result = time.time() - start_time
        print(f"Время выполнения функции: {result} секунд")
        return res

    return wrapper

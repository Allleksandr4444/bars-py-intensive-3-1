import time
from tasks.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def funk_decorator(func):
        def wrapper(*args, **kwargs):
            res = None
            for _ in range(times):
                try:
                    res = func(*args, **kwargs)
                    if res:
                        break
                except:
                    time.sleep(delay)
            else:
                raise MyException

            return res

        return wrapper

    return funk_decorator

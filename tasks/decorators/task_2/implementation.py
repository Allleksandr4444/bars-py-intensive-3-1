from tasks.common import MyException

def cache_func(func):
    cache = {}
    print(cache)

    def wrapper(x):
        nonlocal cache
        print(cache)
        if not cache.get(x):
            result = func(x)
            cache[x] = result
            return result
        else:
            return cache[x]

    return wrapper


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg):
        if isinstance(arg, int) and arg >= 0:
            return func(arg)
        else:
            raise MyException

    return wrapper

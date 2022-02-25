class Multiplier:
    def __init__(self, value):
        self.__number = value

    def get_value(self):

        return int(self.__number)

    def check(func):

        def wrapper(*args):

            for i in args:
                if not isinstance(i, Multiplier):

                    raise Exception('Операнды должны являться дочерним классом Multiplier')

            result = func(*args)

            return result

        return wrapper

    @check
    def __add__(self, other):

        return Multiplier(self.__number + other.__number)

    @check
    def __radd__(self, other):

        return other.__number + self.__number

    @check
    def __sub__(self, other):

        return Multiplier(self.__number - other.__number)

    @check
    def __rsub__(self, other):

        return other.__number - self.__number

    @check
    def __mul__(self, other):

        return Multiplier(self.__number * other.__number)

    @check
    def __rmul__(self, other):

        return other.__number * self.__number

    @check
    def __truediv__(self, other):

        return Multiplier(self.__number / other.__number)

    @check
    def __rtruediv__(self, other):

        return other.__number / self.__number


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        super().__init__(value * 100)


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        super().__init__(value * 1000)


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        super().__init__(value * 1000000)

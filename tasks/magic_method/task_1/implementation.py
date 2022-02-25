class Multiplier:
    def __init__(self, value):
        self.__number = value

    def get_value(self):
        return int(self.__number)

    def __add__(self, other):
        if isinstance(other, Multiplier):
            value = self.__number + other.__number
        else:
            value = self.__number

        return Multiplier(value)

    def __radd__(self, other):
        if isinstance(other, Multiplier):
            value = other.__number + self.__number
        else:
            value = self.__number

        return value

    def __sub__(self, other):
        if isinstance(other, Multiplier):
            value = self.__number - other.__number
        else:
            value = self.__number

        return Multiplier(value)

    def __rsub__(self, other):
        if isinstance(other, Multiplier):
            value = other.__number - self.__number
        else:
            value = self.__number

        return value

    def __mul__(self, other):
        if isinstance(other, Multiplier):
            value = self.__number * other.__number
        else:
            value = self.__number

        return Multiplier(value)

    def __rmul__(self, other):
        if isinstance(other, Multiplier):
            value = other.__number * self.__number
        else:
            value = self.__number

        return value

    def __truediv__(self, other):
        if isinstance(other, Multiplier):
            value = self.__number / other.__number
        else:
            value = self.__number

        return Multiplier(value)

    def __rtruediv__(self, other):
        if isinstance(other, Multiplier):
            value = other.__number / self.__number
        else:
            value = self.__number

        return value


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


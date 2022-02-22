from tasks.common import MyException


class Value:
    def __init__(self, number):
        if not isinstance(number, (int, float)):
            raise MyException
        self.number = number

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise MyException

        return other + self.number

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise MyException

        return self.number + other

    def __sub__(self, other):
        if not isinstance(other, (int, float)):
            raise MyException

        return self.number - other

    def __rsub__(self, other):
        if not isinstance(other, (int, float)):
            raise MyException

        return other - self.number

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise MyException
        return other * self.number

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise MyException
        return self.number * other

    def __truediv__(self, other):
        if not isinstance(other, (int, float)) or other == 0:
            raise MyException

        return self.number / other

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)) or self.number == 0:
            raise MyException

        return other / self.number

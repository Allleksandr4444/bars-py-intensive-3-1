class MathClock:

    def __init__(self, minutes=0):
        self.__minutes = minutes

    def __add__(self, other):
        self.__minutes += other
        return self.__minutes

    def __sub__(self, other):
        self.__minutes -= other
        return self.__minutes

    def __mul__(self, other):
        self.__minutes += other * 60
        return self.__minutes

    def __truediv__(self, other):
        self.__minutes -= other * 60
        return self.__minutes

    def get_time(self):
        hours = (self.__minutes // 60) % 24
        minutes = self.__minutes % 60
        return f"{hours:02d}:{minutes:02d}"

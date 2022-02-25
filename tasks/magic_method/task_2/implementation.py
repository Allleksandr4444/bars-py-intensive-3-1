import datetime


class MathClock:
    def __init__(self):
        date_obj = datetime.datetime(2022, 2, 25)
        self.__time_now = datetime.datetime(year=date_obj.year, month=date_obj.month, day=date_obj.day)

    def get_time(self):
        return self.__time_now.strftime('%H:%M')

    def __add__(self, other):
        if type(other) != int:
            raise 'Введите целое число!'
        time = datetime.timedelta(minutes=int(other))
        self.__time_now += time

    def __sub__(self, other):
        if type(other) != int:
            raise 'Введите целое число!'
        time = datetime.timedelta(minutes=int(other))
        self.__time_now -= time

    def __mul__(self, other):
        if type(other) != int:
            raise 'Введите целое число!'
        time = datetime.timedelta(hours=int(other))
        self.__time_now += time

    def __truediv__(self, other):
        if type(other) != int:
            raise 'Введите целое число!'
        time = datetime.timedelta(hours=int(other))
        self.__time_now -= time


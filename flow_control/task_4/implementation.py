from datetime import (
    date
)


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """

    year = some_date.year
    month = some_date.month
    day = some_date.day

    if month in (1, 3, 5, 7, 8, 10, 12):
        if day == 31:
            if month == 12:
                year += 1
                month = 1
                day = 1
            else:
                month += 1
                day = 1
        else:
            day += 1
    elif month in (4, 6, 9, 11):
        if day == 30:
            month += 1
            day = 1
        else:
            day += 1
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day == 29:
                month += 1
                day = 1
            else:
                day += 1
        else:
            if day == 28:
                month += 1
                day = 1
            else:
                day += 1

    return date(year, month, day)

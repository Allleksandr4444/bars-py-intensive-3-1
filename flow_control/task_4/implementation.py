from datetime import (
     timedelta, date
)


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """

    next_date = some_date + timedelta(days=1)
    return next_date





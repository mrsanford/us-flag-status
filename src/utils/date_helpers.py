from datetime import date
import calendar


def get_nth_weekday(year: int, month: int, weekday_index: int, n: int) -> date:
    """
    Returns the date of the nth occurrence of a weekday in a given month and year.
    ---
    Args:
        :param year: Year (e.g., 2025)
        :param month: Month (1–12)
        :param weekday_index: 0=Monday, 6=Sunday
        :param n: nth occurrence of that weekday
        :return: date object
    """
    count = 0
    for day in range(1, 32):
        try:
            d = date(year, month, day)
        except ValueError:
            break  # invalid day in month
        if d.weekday() == weekday_index:
            count += 1
            if count == n:
                return d
    raise ValueError(f"No {n}th weekday {weekday_index} in {month}/{year}")


def get_last_weekday(year: int, month: int, weekday_index: int) -> date:
    """
    Returns the last occurrence of a weekday in a given month and year.
    ---
    :param year: Year (e.g., 2025)
    :param month: Month (1–12)
    :param weekday_index: 0=Monday, 6=Sunday
    :return: date object
    """
    last_day = calendar.monthrange(year, month)[1]
    for day in range(last_day, 0, -1):
        d = date(year, month, day)
        if d.weekday() == weekday_index:
            return d
    raise ValueError(f"No weekday {weekday_index} found in {month}/{year}")

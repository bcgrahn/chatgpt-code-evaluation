

def thirteenth_friday(month, year):
    """
    Detects if a month contains a Friday with the 13th
    :param month: Month in number
    :param year: Year in four digits
    :return: True if month contains a Friday with the 13th, else False
    """
    from datetime import date
    thirteenth_day = date(year, month, 13)
    if thirteenth_day.strftime('%A') == 'Friday':
        return True
    else:
        return False

def thirteenth_friday(month, year):
    """Detects if a month contains a Friday with the 13th"""
    from datetime import date
    thirteenth_day = date(year, month, 13)
    return bool(thirteenth_day.strftime('%A') == 'Friday')
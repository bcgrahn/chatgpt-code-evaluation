

def detect_13th_Friday(month, year):
    from datetime import date
    thirteenth = date(year, month, 13)
    return thirteenth.weekday() == 4

print(detect_13th_Friday(10, 2020)) # True


def detect_13th_friday(month, year):
  from datetime import date
  thirteenth = date(year, month, 13)
  if thirteenth.weekday() == 4:
    return True
  else:
    return False
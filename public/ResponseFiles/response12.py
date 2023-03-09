

def detect_13th_Friday(month, year):
    # Convert month and year to a datetime object
    date = datetime.datetime(year, month, 1)
    
    # Find the 13th day of the month
    thirteenth = date + datetime.timedelta(days=12)
    
    # Check if it's a Friday
    if thirteenth.weekday() == 4:
        return True
    else:
        return False
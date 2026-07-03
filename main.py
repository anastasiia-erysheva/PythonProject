from datetime import date, timedelta
def num_of_sundays(year):
    d = date(year, 1, 1)
    end = date(year, 12, 31)
    count = 0
    while d <= end:
        if d.weekday() == 6:
            count += 1
        d = d + timedelta(days=1)
    return count

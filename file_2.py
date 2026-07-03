from datetime import datetime, timedelta, date
birthday = datetime.strptime(input(), "%d.%m.%Y").date()
today = date.today()
birthday_this_year = date(today.year, birthday.month, birthday.day)
if birthday_this_year > today:
    years = today.year - birthday.year - 1
    next_birthday = date(today.year, birthday.month, birthday.day)
else:  # ДР уже прошёл или сегодня
    years = today.year - birthday.year
    next_birthday = date(today.year + 1, birthday.month, birthday.day)
days_left = (next_birthday - today).days
print(f"Полных лет: {years}")
print(f"До следующего дня рождения: {days_left} дней")




import calendar
number = input()
try:
    number = int(number)
    if 1 <= number <= 12:
        print(calendar.month_name[number])
    else:
        print("Введено число из недопустимого диапазона")
except ValueError:
    print("Введено некорректное значение")

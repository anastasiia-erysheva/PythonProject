def get_weekday(number):
    week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if 1 > number or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return week[number]

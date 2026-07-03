try:
    x = int(input())

    if x < 0:
        raise ValueError("Введите положительное число")
    if x == 0:
        raise ZeroDivisionError("Делить на ноль нельзя")
    result = 100 / x
    print(result)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
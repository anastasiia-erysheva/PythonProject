f = input()
a, b = map(int, input().split())
values = [eval(f) for x in range(a, b + 1)]
min_values = min(values)
max_values = max(values)
print(f"Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min_values}")
print(f"Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max_values}")
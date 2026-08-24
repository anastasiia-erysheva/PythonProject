def calculate_bmi(weight, height):
    # Весь расчет должен быть внутри функции
    bmi = weight / (height ** 2)
    return round(bmi, 1)

# Теперь мы запрашиваем данные у пользователя
user_weight = int(input("Введите вес в кг: "))
user_height = float(input("Введите рост в метрах (например, 1.7): "))

# Вызываем функцию и передаем ей введенные данные
result = calculate_bmi(user_weight, user_height)

print(f"Ваш ИМТ: {result}")
import json
name_file = input()
try:
    with open(name_file, "r", encoding = "utf-8") as f:
        result = json.load(f)
        print(result)
except json.decoder.JSONDecodeError:
    print("Ошибка при десериализации")
except FileNotFoundError:
    print("Файл не найден")






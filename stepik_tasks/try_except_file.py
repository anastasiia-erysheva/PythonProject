name_file = input()
try:
    with open(name_file, encoding= "utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден")



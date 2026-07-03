import json

try:
    with open("factory_data.json", "r", encoding="utf-8") as file:
        boxes = json.load(file)

except json.JSONDecodeError:
    print("Файл пустой")
    boxes = []

except FileNotFoundError:
    print("Файла вообще нет на диске")
    boxes = []
    defective_id = []
    for box in boxes:
        if box["status"] == "брак":
            defective_id.append(box["id"])
    print(defective_id)
import csv
import json
total = 0
with open("prices.json", "r", encoding="utf-8") as file:
    data = json.load(file)
for i in range(1, 5):
    with open(f"quarter{i}.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row["продукт"]
            kg_sold = sum(int(x) for x in list(row.values())[1:])
            total += kg_sold * data[product]
print(total)


import csv
import json
from collections import Counter
with open("prices.json", "r", encoding="utf-8") as file:
    data = json.load(file)
for i in range(1, 5):
    with open(f"quarter{i}.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:



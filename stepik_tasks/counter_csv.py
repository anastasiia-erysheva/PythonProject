import csv
from collections import Counter
with open("name_log.csv", "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    result = []
    for row in reader:
        mail = row["email"]
        result.append(mail)
counted = Counter(result)
for mail, count in sorted(counted.items()):
    print(f"{mail}: {count}")


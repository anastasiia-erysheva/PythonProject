from collections import Counter
with open("pythonzen.txt", "r", encoding="utf-8") as file:
    text = file.read()
text = text.lower()
text_filtre = [char for char in text if char.isalpha()]
counter = Counter(text_filtre)
for key, value in sorted(counter.items()):
    print(f"{key}: {value}")
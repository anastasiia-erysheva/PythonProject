from collections import Counter
word = input().lower().split()
counter = Counter(word)
result = []
max_quantity = max(counter.values())
for key, value in counter.items():
    if value == max_quantity:
        result.append(key)
print(max(result))
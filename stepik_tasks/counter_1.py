from collections import Counter
word = input().lower().split(',')
counter = Counter(word)
max_len = max(len(w) for w in counter)
for item, count in sorted(counter.items()):
    price = sum(ord(char) for char in item if char != " ")
    total_price = price * count
    print(f"{item:<{max_len}}: {price} UC x {count} = {total_price} UC")

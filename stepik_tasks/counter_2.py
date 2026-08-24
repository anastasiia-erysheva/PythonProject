from collections import Counter
lengths = [len(w) for w in input().split()]
counts = Counter(lengths)
sorted_lengths = sorted(counts.keys(), key=lambda x: (counts[x], lengths.index(x)))
for item in sorted_lengths:
    print(f"Слов длины {item}: {counts[item]}")
from collections import Counter
counter = Counter(list(map(int, input().split())))
n = int(input())
total = 0
for _ in range(n):
    class_num, price = list(map(int, input().split()))
    if counter[class_num] > 0:
        counter[class_num] -= 1
        total += price
print(total)

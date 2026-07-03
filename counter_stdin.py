import sys
result = []
for line in sys.stdin:
    item = line.strip().split(" ")
    result.append((int(item[1]), item[0]))
result.sort()
print(result[1][1])

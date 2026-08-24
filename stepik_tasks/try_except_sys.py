import sys
total = 0
count_bad = 0
for line in sys.stdin:
    try:
        number = int(line)
        total += number
    except ValueError:
        try:
            number = float(line)
            total += number
        except ValueError:
            count_bad += 1
print(total)
print(count_bad)
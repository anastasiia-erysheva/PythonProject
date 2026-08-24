import sys
count = 0
for line in sys.stdin:
    tokens = line.split()
    for t in tokens:
        try:
            x = int(t)
            if count == 0:
                min_val = x
                max_val = x
            else:
                if x < min_val:
                    min_val = x
                if x > max_val:
                    max_val = x
            count += 1
        except ValueError:
            print("Ошибка:", t, file = sys.stderr)

print(min_val, max_val, count)
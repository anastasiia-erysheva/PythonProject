def alternating_sequence(count=None):
    current = 1
    yielded_count = 0
    while True:
        if current % 2 == 0:
            yield -current
        else:
            yield current

        yielded_count += 1
        current += 1

        if count is not None and yielded_count == count:
            break

generator = alternating_sequence(10)

print(*generator)
def get_min_max(iterable):
    it = iter(iterable)
    first = next(it, None)
    if first is None:
        return None

    min_value = first
    max_value = first

    for item in it:
        if item < min_value:
            min_value = item
        elif item > max_value:
            max_value = item

    return (min_value, max_value)

iterable = iter(range(10000000))

print(get_min_max(iterable))


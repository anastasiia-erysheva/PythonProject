def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    return numbers[start] + range_sum(numbers, (start + 1), end)
(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
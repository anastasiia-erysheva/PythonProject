def filter_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num
def squares(numbers):
        for num in numbers:
            yield num * 3
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total
list_numbers = [2, -3, 4, 1, -5, 6]
pipeline = running_sum(squares(filter_numbers(list_numbers)))
for value in pipeline:
    print(value)
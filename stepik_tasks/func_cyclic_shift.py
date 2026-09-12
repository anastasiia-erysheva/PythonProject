def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step = step % len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)
import random


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        self.count += 1
        return random.randint(self.left, self.right)
iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
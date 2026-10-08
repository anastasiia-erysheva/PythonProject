class Square:
    def __init__(self, n):
        self.n = n
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > self.n:
            raise StopIteration
        result = self.num ** 2
        self.num += 1
        return result
squares = Square(10)

print(list(squares))


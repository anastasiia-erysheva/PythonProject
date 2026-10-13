class SquaresIterator:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.n:
            raise StopIteration
        res = self.num ** 2
        self.num += 1
        return res


if __name__ == "__main__":
    iterator = SquaresIterator(3)

    for number in iterator:
        print(number)
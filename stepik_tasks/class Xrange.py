class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.end:
                raise StopIteration
        else:
            if self.current <= self.end:
                raise StopIteration

        current_value = self.current
        self.current += self.step
        return current_value
xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')



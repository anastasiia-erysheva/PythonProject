def triangle(h):
    def rec(size):
        if size <= 0:
            return
        else:
            print("*" * size)
            rec(size - 1)
    rec(h)
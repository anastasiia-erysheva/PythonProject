def func_rec(n):
    spaces = 2 * (n - 1)
    digits_count = 4 * (5 - n)
    print(" " * spaces + str(n) * digits_count)
    if n == 4:
        return
    func_rec(n + 1)
    print(" " * spaces + str(n) * digits_count)


func_rec(1)



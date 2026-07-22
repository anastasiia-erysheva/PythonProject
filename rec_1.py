def rec():
    num = int(input())
    if num == 0:
        print(num)
    else:
        rec()
        print(num)
rec()
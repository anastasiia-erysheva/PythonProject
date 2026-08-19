s = input()
result = eval(s)
if isinstance(result, list):
    print(result[-1])
elif isinstance(result, tuple):
    print(result[0])
else:
    print(len(result))

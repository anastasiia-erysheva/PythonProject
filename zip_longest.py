def zip_longest(*args, fill=None):
    max_list = max(len(lst) for lst in args)
    result = []

    for i in range(max_list):
        current = []

        for j in args:
            if i < len(j):
                current.append(j[i])
            else:
                current.append(fill)

        result.append(tuple(current))

    return result
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))



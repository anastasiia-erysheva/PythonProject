def recursive_sum(nested_lists):
    if not nested_lists:
        return 0
    total = 0
    for item in nested_lists:
        if type(item) is list:
            total += recursive_sum(item)
        if type(item) is int:
            total += item
    return total
my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))


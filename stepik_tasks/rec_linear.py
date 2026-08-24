def linear(nested_lists):
    if not nested_lists:
        return []
    result = []
    for item in nested_lists:
        if isinstance(item, list):
            result.extend(linear(item))
        if isinstance(item, int):
            result.append(item)
    return result
my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))
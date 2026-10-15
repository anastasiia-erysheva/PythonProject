def flatten_and_double(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_and_double(item)
        else:
            yield item * 2
nested_list = [1, [2, [3, 4], 5], [6, [7, [8, 9]]]]
result_list = list(flatten_and_double(nested_list))
print(result_list)
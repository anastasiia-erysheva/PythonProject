def get_all_values(nested_dicts, key):
    result = set()
    if not nested_dicts:
        return set()
    if key in nested_dicts:
        result.add(nested_dicts[key])
    for item in nested_dicts:
        if type(nested_dicts[item]) is dict:
            result.update(get_all_values(nested_dicts[item], key))
    return result
my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
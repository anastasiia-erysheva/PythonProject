def dict_travel(nested_dicts, path=""):
    if not nested_dicts:
        return

    for item in sorted(nested_dicts):
        if type(nested_dicts[item]) is dict:
            if not path:
                new_path = item
            else:
                new_path = path + "." + item
            dict_travel(nested_dicts[item], new_path)

        else:
            if not path:
                print(f"{item}: {nested_dicts[item]}")
            else:
                print(f"{path}.{item}: {nested_dicts[item]}")

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)



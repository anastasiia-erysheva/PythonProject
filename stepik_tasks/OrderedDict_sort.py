from collections import OrderedDict
def custom_sort(ordered_dict, by_values = False):
    sort_key = lambda x: x[1] if by_values else x[0]
    sorted_items = sorted(ordered_dict.items(), key=sort_key)
    ordered_dict.clear()
    for key, value in sorted_items:
        ordered_dict[key] = value
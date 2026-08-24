def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for v in nested_dicts:
        if type(nested_dicts[v]) == dict:
            value = get_value(nested_dicts[v], key)
            if value is not None:
                return value
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))


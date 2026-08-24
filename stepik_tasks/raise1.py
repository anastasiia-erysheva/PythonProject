def get_id(names, name):
    if not type(name) == str:
        raise TypeError('Имя не является строкой')
    if not name[0].isupper() or not name[1:].islower() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names) + 1

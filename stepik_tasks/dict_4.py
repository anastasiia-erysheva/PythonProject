def hash_as_key(object):
    result = {}
    for obj in object:
        h_key = hash(obj)
        if h_key not in result:
            result[h_key] = obj
        elif isinstance(result[h_key], list):
            result[h_key].append(obj)
        else:
            result[h_key] = [result[h_key], obj]
    return result
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))
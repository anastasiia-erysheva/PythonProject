from collections import ChainMap
def get_all_values(chainmap, key):
    result = set()
    chainmap_list = chainmap.maps
    for d in chainmap_list:
        if key in d:
            result.add(d[key])
    return result


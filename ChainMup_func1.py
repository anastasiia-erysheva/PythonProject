from collections import ChainMap
def get_value(chainmap, key, from_left = True):
    maps_order = (chainmap.maps if from_left else reversed(chainmap.maps))
    for d in maps_order:
        if key in d:
            return d[key]



from collections import ChainMap
def count_occurrences(chainmap, key):
    total = 0
    for d in chainmap.maps:
        if key in d:
            total += 1
    return total

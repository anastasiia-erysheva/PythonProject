from collections import ChainMap
def find_conflicts(chainmap):
    conflicts = []
    k = set(chainmap.keys())
    for key in k:
        values = set()
        for d in chainmap.maps:
            if key in d:
                values.add(d[key])
        if len(values) > 1:
            conflicts.append(key)
    return sorted(conflicts)


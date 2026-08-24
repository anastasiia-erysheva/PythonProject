from collections import Counter
data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
def get_min_values():
    if not data:
        return []
    min_val = min(data.values())
    return [item for item in data.items() if item[1] == min_val]

def get_max_values():
    if not data:
        return []
    max_val = max(data.values())
    return [item for item in data.items() if item[1] == max_val]
data.min_values = get_min_values
data.max_values = get_max_values



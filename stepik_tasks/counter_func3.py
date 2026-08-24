from collections import Counter
def print_bar_chart(data, mark):
    data = Counter(data)
    max_key = max(len(k) for k in data.keys())
    for key, value in data.most_common():
        print(f"{key.ljust(max_key)} |{mark * value}")


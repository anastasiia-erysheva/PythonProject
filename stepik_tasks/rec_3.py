n = list(map(int, input().split()))
def get_rec_sum(n, index):
    if index == len(n):
        return 0
    else:
        return n[index] + get_rec_sum(n, index + 1)
print(get_rec_sum(n, 0))






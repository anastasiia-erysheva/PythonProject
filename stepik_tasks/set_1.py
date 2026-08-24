n = int(input())
result_set =set(input().split(", "))
for i in range(n-1):
    next_set = set(input().split(", "))
    result_set = result_set.intersection(next_set)
if len(result_set) == 0:
    print("Сериал снять не удастся")
else:
    # sorted() делает список по алфавиту, а join() склеивает его через ", "
    print(", ".join(sorted(result_set)))
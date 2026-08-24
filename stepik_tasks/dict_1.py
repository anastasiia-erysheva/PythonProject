s = input().lower()
symbols = ".,!?:;-"
for char in symbols:
    s = s.replace(char, "")
words = s.split()
count_dict ={}
for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1
min_count = min(count_dict.values())
result = [w for w in count_dict if count_dict[w] == min_count]
final_word = min(result)
print(final_word)
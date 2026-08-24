from collections import Counter
def count_occurrences(word, words):
    target_word = word.lower()
    words = words.lower().split(" ")
    counter = Counter(words)
    return counter[target_word]


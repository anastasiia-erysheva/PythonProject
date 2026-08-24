from collections import Counter
def scrabble(symbols, word):
    counter_sym = Counter(symbols.lower())
    counter_word = Counter(word.lower())
    if counter_sym >= counter_word:
        return True
    else:
        return False


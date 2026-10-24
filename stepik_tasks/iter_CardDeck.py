class CardDeck:
    suits = ("пик", "треф", "бубен", "червей")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
    def __init__(self):
        self.count = 0
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(f"{rank} {suit}")
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= len(self.cards):
            raise StopIteration
        else:
            result = self.cards[self.count]
            self.count += 1
            return result
cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])



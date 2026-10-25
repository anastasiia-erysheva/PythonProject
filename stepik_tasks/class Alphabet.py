class Alphabet:
    def __init__(self, language):
        self.data = {
            'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
            'en': 'abcdefghijklmnopqrstuvwxyz',
        }
        self.iterable = self.data[language]
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)
en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

import pickle
from collections import namedtuple
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open("data.pkl", mode = "rb") as file:
    animal_list = pickle.load(file)
    for animal in animal_list:
        for field, value in zip(animal._fields, animal):
            print(f"{field}: {value}")
        print()


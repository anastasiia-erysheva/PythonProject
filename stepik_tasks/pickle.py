import sys
import pickle
lines = sys.stdin.read().splitlines()
file_name = lines[0]
arguments = lines[1:]
with open(file_name, "rb") as f:
    my_func = pickle.load(f)
    print(my_func(*arguments))

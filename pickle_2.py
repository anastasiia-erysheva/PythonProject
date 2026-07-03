import sys
import pickle
filename = sys.stdin.readline().strip()
expected_sum = int(sys.stdin.readline().strip())
with open(filename, "rb") as file:
    data = pickle.load(file)
checksum = 0
if type(data) == dict:
    for key in data:
        if type(key) == int:
            checksum += key
elif type(data) == list:
    num_list = []
    for elem in data:
        if type(elem) == int:
            num_list.append(elem)
    if num_list:
        checksum = min(num_list) * max(num_list)
if checksum == expected_sum:
    print("Контрольные суммы совпадают")
else:
    print("Контрольные суммы не совпадают")



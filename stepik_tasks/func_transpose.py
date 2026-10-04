def transpose(matrix):
    res_lst =[list(lst) for lst in zip(*matrix)]
    return res_lst

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

for row in transpose(matrix):
    print(row)

array = [
    [-1,  4, -5, -9,  3],
    [ 6, -4, -7,  4, -5],
    [ 3,  5,  0, -9, -1],
    [ 1,  5, -7, -8, -9],
    [-3,  2,  1, -5,  6]
]
def matrix (array):
    new_array = [row[:]for row in array]
    for i in range(len(new_array)):
        if new_array[i][i] <0:
            new_array[i][i] = 0
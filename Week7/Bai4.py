import math


def read_file(file):
    with open(file, 'r') as f:
        filename = f.read().split()
        A = (float(filename[1]), float(filename[2]))
        B = (float(filename[4]), float(filename[5]))
        return A, B


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


A, B = read_file('input')
f = open('output.txt', "w")
f.write(str(round(distance(A, B), 2)))

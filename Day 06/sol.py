import sys
from functools import reduce
from math import floor, ceil, sqrt

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

data = open(input_file).read().split('\n')

def f(z):
    t, d = z
    if t**2 < 4*d:
        return 0
    x1 = t + sqrt(t**2 - 4 * d)
    x1 /= 2
    x2 = t - sqrt(t**2 - 4 * d)
    x2 /= 2
    
    c = ceil(x1 - 1) - floor(x2 + 1) + 1
    return c


def part1(data):
    t = map(int, data[0].split()[1:])
    d = map(int, data[1].split()[1:])
    x = map(f, zip(t, d))
    y = reduce(lambda acc, i: acc * i, x, 1)
    print(y)


def part2(data):
    t = int(''.join(data[0].split()[1:]))
    d = int(''.join(data[1].split()[1:]))
    y = f((t, d))
    print(y)
    
part1(data)
part2(data)
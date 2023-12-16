import re
import sys
from collections import defaultdict
from functools import reduce
from math import lcm

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'


def parse(acc, line):
    pattern = r"(\w+) = \((\w+), (\w+)\)"
    r = re.match(pattern, line)
    u, left, right =  r.groups()
    acc[u] = {'L': left, 'R': right}
    return acc

with open(input_file, 'r') as f:
    ops = f.readline().strip()
    f.readline()
    lines = f.read().split('\n')

G = reduce(parse, lines, {})
n = len(ops)

def part1():
    u = 'AAA'
    e = 'ZZZ'
    step = 0
    while u != e:
        u = G[u][ops[step % n]]
        step += 1
    print(step)


def go(u):
    step = 0
    while u[2] != 'Z':
        u = G[u][ops[step % n]]
        step += 1
    return step

def part2():
    step = 1
    for u in G.keys():
        if u[2] == 'A':
            step = lcm(step, go(u))

    print(step)

part1()
part2()
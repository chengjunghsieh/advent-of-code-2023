import sys
from collections import deque
from functools import reduce

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    data = f.readlines()

n = len(data)
m = len(data[0].strip())
G = {(i, j): c for i, r in enumerate(data) for j, c in enumerate(r.strip())}

U, R, D, L = 0, 1, 2, 3
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def apply(u, d):
    return (u[0] + d[0], u[1] + d[1])

def get(u, d):
    match G[u]:
        case '.':
            return [(apply(u, DIRS[d]), d)]
        case '-':
            if d in (L, R):
                return [(apply(u, DIRS[d]), d)]
            return [(apply(u, DIRS[L]), L), (apply(u, DIRS[R]), R)]
        case '|':
            if d in (U, D):
                return [(apply(u, DIRS[d]), d)]
            return [(apply(u, DIRS[U]), U), (apply(u, DIRS[D]), D)]
        case '/':
            return [(apply(u, DIRS[d^3]), d^3)]
        case '\\':
            return [(apply(u, DIRS[d^1]), d^1)]

def solve(s, d):
    Q = deque()
    Q.append((s, d))
    seen = {(s, d)}

    while Q:
        u, d = Q.popleft()
        vec = get(u, d)
        for v in vec:
            if v[0] in G and v not in seen:
                seen.add(v)
                Q.append(v)

    return len(set(i for i, _ in seen))

print(solve((0, 0), R))
print(max(solve(s ,d) for d in (U, R, D, L) for s in G if apply(s, DIRS[d^2]) not in G))
import sys
from collections import Counter

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()

maze = {complex(i, j): c for i, r in enumerate(lines)
                         for j, c in enumerate(r.strip())}
U, D, L, R = -1, +1, -1j, +1j
dirs = {'|': (U, D), '-': (L, R), 'J': (U, L), 'L': (U, R), '7': (D, L), 'F': (D, R), '.': (), 'S': (U, D, L, R)}

G = {k: {k + v for v in dirs[c]} for k, c in maze.items()}
vis = {k for k, c in maze.items() if c == 'S'}
que = list(vis)
for u in que:
    nxt = G[u] - vis
    nxt = set((filter(lambda i: i in maze and maze[i] != '.', nxt)))
    vis |= nxt
    que += list(nxt)
print(len(vis) // 2)


# an point inside the shape corsses the border an odd of times
# in this problem watch horizontal border is enough
cross = lambda n: [complex(n.real, i) for i in range(int(n.imag))]

print(sum(
    sum(x in vis and maze[x] in "|JLS" for x in cross(p)) % 2
    for p in set(maze) - vis))
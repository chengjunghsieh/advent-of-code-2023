import sys

from heapq import heapify, heappush, heappop

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    data = f.readlines()

G = {(i, j): int(c) for i, r in enumerate(data) for j, c in enumerate(r.strip())}

U, R, D, L = 0, 1, 2, 3
DIRS = {
    U: (1, 0), R: (0, 1),
    D: (-1, 0), L: (0, -1)
}

n = len(data)
m = len(data[0].strip())

def solve(min_step, max_step):
    s = (0, 0)
    t = (n - 1, m - 1)
    
    Q = [(0, s, U), (0, s, R)]
    heapify(Q)  # pq is already sorted, just for readability
    dist = {}
    
    while Q:
        w, u, d = heappop(Q)
        if u == t:
            return w
        if (u, d) in dist and dist[u, d] != w:
            continue
        dist[u, d] = w
        x, y = u
        dx, dy = DIRS[d]
        for i in (1, -1):
            nd = (d + i) % 4
            for k in range(min_step, max_step + 1):
                nx = x + dx*k
                ny = y + dy*k
                if (nx, ny) in G:
                    nw = w + sum(G[(x+dx*j, y+dy*j)] for j in range(1, k+1))
                    if ((nx, ny), nd) not in dist or dist[(nx, ny), nd] > nw:
                        dist[(nx, ny), nd] = nw
                        heappush(Q, (nw, (nx, ny), nd))

print(solve(1, 3))
print(solve(4, 10))

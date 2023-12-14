import re
import sys

argv = sys.argv

input_file = 'input.txt'
if 'D' in argv:
  input_file = 'sample.txt'


grid = []
with open(input_file, 'r') as f:
  for i in f:
    grid.append(i.strip())

n = len(grid)
m = len(grid[0])

def is_symbol(c):
  return c != '.' and not c.isdigit()

def part1():
  vis = [[0 for j in range(m)] for i in range(n)]
  que = [[i, j] for i in range(n) for j in range(m) if is_symbol(grid[i][j])]

  for u in que:
    for i in [-1, 0, 1]:
      for j in [-1, 0, 1]:
        x, y = u
        x += i
        y += j
        if not (x >= 0 and x < n and y >= 0 and y < m):
          continue
        if grid[x][y] == '.' or is_symbol(grid[x][y]):
          continue
        vis[x][y] = 1

  # print(grid)
  # print(vis)
  ans = 0
  for i in range(n):
    s = ''
    ok = False
    line = []
    for j in range(m):
      if grid[i][j].isdigit():
        s += grid[i][j]
        ok |= vis[i][j]
      else:
        if len(s) > 0 and ok:
          line.append(s)
          ans += int(s)
        s = ''
        ok = False
    
    if len(s) > 0 and ok:
      line.append(s)
      ans += int(s)
  print(ans)

def part2():
  symbols = {(i, j): [] for i in range(n) for j in range(m) if grid[i][j] == '*'}
  
  for i, row in enumerate(grid):
    for j in re.finditer(r'\d+', row):
      pos = {(r, c) for r in (i - 1, i, i + 1)
                    for c in range(j.start() - 1, j.end() + 1)}
      for k in (pos & symbols.keys()):
        symbols[k].append(int(j.group()))

  print(sum(i[0] * i[1] for i in symbols.values() if len(i) == 2))

part1()
part2()
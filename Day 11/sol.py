import sys

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()
    maze = map(lambda l: l.strip().replace('.', '0').replace('#', '1'), lines)

maze = list(map(lambda l: [int(i) for i in l], maze))

tot = sum([sum(i) for i in maze])

def rotate(mat):
    return [row[::-1] for row in zip(*mat)]


def dist(mat, n):
    ans = 0
    lst = -1
    num = 0
    for i, row in enumerate(mat):
        if any(row):
            if lst >= 0:
                ans += ((i - lst - 1) * n + 1) * num * (tot - num)
            lst = i
            num += sum(row)
    return ans

print(dist(maze, 2) + dist(rotate(maze), 2))
print(dist(maze, 1000000) + dist(rotate(maze), 1000000))

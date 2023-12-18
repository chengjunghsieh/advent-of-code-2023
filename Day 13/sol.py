import sys

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    data = f.read().split('\n\n')

def find_mirror(data, diff=0):
    G = data.split('\n')
    for i in range(1, len(G)):
        if sum(
            a != b for j, k in zip(G[i - 1::-1], G[i:])
                for a, b in zip(j,k)
        ) == diff:
            return i        

    return 0

def solve(data, diff=0):
    if i:=find_mirror(data, diff):
        return i*100

    x = '\n'.join(map(''.join, zip(*data.splitlines())))
    if i:=find_mirror(x, diff):
        return i

    raise Exception(-1)


print(sum(solve(i, 0) for i in data))
print(sum(solve(i, 1) for i in data))
import sys

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'


def solve(line):
    arr = list(map(int, line.split()))    
    diff = lambda a: [j - i for i, j in zip(a, a[1:])]
    rec = lambda l: l[-1] + rec(diff(l)) if any(l) else 0
    return rec(arr)

def solve2(line):
    arr = list(map(int, line.split()))    
    diff = lambda a: [j - i for i, j in zip(a, a[1:])]
    rec = lambda l: l[0] - rec(diff(l)) if any(l) else 0
    return rec(arr)

with open(input_file, 'r') as f:
    ans, ans2 = 0, 0
    for line in f:
        ans += solve(line.strip())
        ans2 += solve2(line.strip())
    print(ans)
    print(ans2)

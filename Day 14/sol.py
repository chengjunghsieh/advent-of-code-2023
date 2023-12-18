import sys

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    data = f.read()

def rotate90(data):
    return list((map(lambda l: ''.join(reversed(l)), zip(*data))))

def rotate180(data):
    return rotate90(rotate90(data))

def rotate270(data):
    return rotate90(rotate180(data))

def tilt(line):
    return '#'.join((''.join(sorted(p)) for p in line.split('#')))

def move_east(data):
    return [tilt(l) for l in data]

def move_north(data):
    return rotate270(move_east(rotate90(data)))

def move_west(data):
    return rotate180(move_east(rotate180(data)))

def move_south(data):
    return rotate90(move_east(rotate270(data)))

def compute(data):
    return sum(r * row.count('O') for r, row in enumerate(data[::-1], 1))

def do_n_times(f, x, n):
    seen = {}
    for i in range(n):
        if x in seen:
            break
        seen[x] = i
        x = f(x)
    else:
        return x
    cycle_start = seen[x]
    cycle_len = i - seen[x]
    rem = (n - i) % cycle_len
    return do_n_times(f, x, rem)

def do_cycle(data):
    data = list(map(lambda l: l.strip(), data.splitlines()))
    data = move_east(move_south(move_west(move_north(data))))
    return '\n'.join(data)

def part1(data):
    data = list(map(lambda l: l.strip(), data.splitlines()))
    G = move_north(data)
    print(compute(G))
 
def part2(data):
    G = do_n_times(do_cycle, data, 1_000_000_000)
    G = list(map(lambda l: l.strip(), G.splitlines()))
    print(compute(G))

part1(data)
part2(data)
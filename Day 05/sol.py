import sys

from functools import reduce

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

seeds, *mappings = open(input_file).read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

def chain(start, mapping):
    for m in mapping.split('\n')[1:]:
        dst, src, len = map(int, m.split())
        delta = start - src
        if delta in range(len):
            return dst + delta
    else: return start

print(min(reduce(chain, mappings, s) for s in seeds))

def f2(seeds, mapping):
    mapping = mapping.split('\n')[1:]
    for start, length in seeds:
        while length > 0:
            for m in mapping:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else:
                yield (start, length)
                break

seeds2 = zip(seeds[0::2], seeds[1::2])
ans2 = min(reduce(f2, mappings, seeds2))[0]
print(ans2)
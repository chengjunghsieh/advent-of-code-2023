import sys

from functools import cache

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    data = f.readlines()

def part1(data):
    S, M = data
    S += '.'
    M = eval(M)
    return S, M

def part2(data):
    S, M = data
    S = (S + '?') * 4 + S + '.'
    M = eval(M) * 5
    return S, M

def solve(parser):
    def f(data):
        S, M = parser(data)
        @cache
        def dp(i, j):
            if i == len(S):
                return j == len(M)

            res = 0
            # '?' is '.'
            if S[i] in ".?":
                res += dp(i + 1, j)

            try:
                k = i + M[j]
                # S[i...k] is '#'
                if '.' not in S[i:k] and S[k] != '#':
                    res += dp(k + 1, j+1) # needs to be k + 1 to make S[k] = '.' if S[k] = '?'
            except IndexError:
                pass 

            return res

        return dp(0, 0)

    return f

data = list(map(lambda l: l.strip().split(), data))
print(sum(map(solve(part1), data)))
print(sum(map(solve(part2), data)))
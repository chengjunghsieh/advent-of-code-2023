import sys

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

with open(input_file, 'r') as f:
    ans = 0
    copies = []
    for line in f:
        _, nums = line.split(':')
        winning, hands = nums.split('|')
        winning = set(map(int, filter(lambda s: s != "", winning.strip().split(' '))))
        hands = set(map(int, filter(lambda s: s != "", hands.strip().split(' '))))
        intersect = winning & hands
        n = len(intersect)
        copies.append(n)
        if n > 0:
            ans += 1 << (n - 1)
    print(ans)

    n = len(copies)
    cnt = [0] * n
    ans2, acc = 0, 1
    for i, j in enumerate(copies):
        acc += cnt[i]
        ans2 += acc
        if (i + 1 < n):
            cnt[i + 1] += acc
        if (i + j + 1 < n):
            cnt[i + j + 1] -= acc
    print(ans2)

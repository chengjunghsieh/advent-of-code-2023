import sys

argv = sys.argv

input_file = './input.txt'
if 'D' in argv:
    input_file = './sample.txt'

def eval(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    best = max(score(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)

def score(hand):
    return sorted(map(hand.count, hand), reverse=True)

for face in 'ABCDE', 'A0CDE':
    print(sum(rank * bid for rank, (*_, bid) in
        enumerate(sorted(map(eval, open(input_file))), start=1)))
def part1(f):
  red = 12
  green = 13
  blue = 14
  ans = 0
  for line in f:
    game, sets = line.strip().split(':')
    _, id = game.split(' ')
    sets = sets.split(';')
    ok = True
    for s in sets:
      for i in s.strip().split(','):
        n, color = i.strip().split(' ')
        n = int(n)
        if (color == 'blue' and n > blue) or \
          (color == 'red'and n > red) or \
          (color == 'green' and n > green):
          ok = False
    if ok:
      ans += int(id)
  print(ans)

def part2(f):
  ans = 0
  for line in f:
    game, sets = line.strip().split(':')
    _, id = game.split(' ')
    sets = sets.split(';')
    
    red = 1
    green = 1
    blue = 1
    for s in sets:
      for i in s.strip().split(','):
        n, color = i.strip().split(' ')
        n = int(n)
        if color == 'red':
          red = max(red, n)
        if color == 'green':
          green = max(green, n)
        if color == 'blue':
          blue = max(blue, n)
    power = red * green * blue
    ans += power
  print(ans)

with open('./sample.txt', 'r') as f:
  # part1(f)
  part2(f)

with open('./input.txt', 'r') as f:
  # part1(f)
  part2(f)

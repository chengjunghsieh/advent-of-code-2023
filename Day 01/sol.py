def part1():
    with open('./input.txt', 'r') as f:
        ans = 0
        for line in f:
            num = ''
            for i in line:
                if i.isdigit():
                    num += i
            ans += int(num[0] + num[-1])
        print(ans)


def get_positions(string, substring):
    return [index for index, _ in enumerate(string) if string[index:index + len(substring)] == substring]


def part2():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open('./input.txt', 'r') as f:
        ans = 0
        for line in f:
            x, y = len(line), -1
            fi, se = '', ''
            for j, i in enumerate(nums):
                positions = get_positions(line, i)
                if len(positions) > 0:
                    if x > positions[0]:
                        x = positions[0]
                        fi = nums[j - 9] if j >= 9 else nums[j]
                    if y < positions[-1]:
                        y = positions[-1]
                        se = nums[j - 9] if j >= 9 else nums[j]
            ans += int(fi + se)
        print(ans)

# part1()
part2()


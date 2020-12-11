from itertools import combinations


def part1(data):
    for i in range(25, len(data)):
        sums = {sum(combination): combination for combination in combinations(data[i-25:i], 2)}
        if data[i] not in sums:
            return data[i]


def part2(data):
    num = part1(data)
    sum_length = 2
    while sum_length < len(data) - sum_length:
        for i in range(len(data)):
            if sum(data[i:i+sum_length]) == num:
                return min(data[i:i+sum_length]) + max(data[i:i+sum_length])
        sum_length += 1


data = list(map(int, open("day9.in").read().splitlines()))
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


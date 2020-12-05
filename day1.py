from itertools import combinations


def part1(data):
    for comb in combinations(data, 2):
        if sum(comb) == 2020:
            return comb[0] * comb[1]


def part2(data):
    for comb in combinations(data, 3):
        if sum(comb) == 2020:
            return comb[0] * comb[1] * comb[2]
    

data = open("day1.in").read().splitlines()
data = sorted(list(map(int, data)))

res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


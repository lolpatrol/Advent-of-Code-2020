

def part1(data):
    return sum(len(set(g.replace("\n", ""))) for g in data)
    
    
def part2(data):
    return sum(1 for g in data for q in set(g.replace("\n", "")) if g.count(q) == len(g.splitlines()))

    
data = open("day6.in").read().split("\n\n")
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


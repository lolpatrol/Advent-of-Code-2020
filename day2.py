

def part1(data):
    return sum(1 for l in data if int(l[0]) <= l[3].count(l[2]) <= int(l[1]))
    
    
def part2(data):
    lo, hi = lambda a: int(a[0])-1, lambda b: int(b[1])-1
    return sum(1 for l in data if l[3][lo(l)] != l[3][hi(l)] and l[2] in [l[3][lo(l)], l[3][hi(l)]])

    
data = open("day2.in").read().splitlines()
data = [line.replace(":", "").replace("-", " ").split(" ") for line in data]
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


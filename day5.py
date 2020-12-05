

def part1(data):
    highest = 0
    for line in data:
        row, col = line[:7], line[7:]
        rr = bisect(row, [i for i in range(128)])
        cc = bisect(col, [i for i in range(8)])

        if rr * 8 + cc > highest:
            highest = rr * 8 + cc

    return highest

    
def part2(data):
    all = []
    for line in data:
        row, col = line[:7], line[7:]
        rr = bisect(row, [i for i in range(128)])
        cc = bisect(col, [i for i in range(8)])
        all.append(rr * 8 + cc)
    all.sort()
    for i in range(1, len(all)):
        if all[i] != all[i-1] + 1:
            return all[i] - 1


def bisect(line, vec):
    for r in line:
        if r in ["F", "L"]:
            vec = vec[0:int(len(vec) / 2)]
        else:
            vec = vec[int(len(vec) / 2):]
    return vec[0]

    
data = open("day5.in").read().splitlines()

#data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


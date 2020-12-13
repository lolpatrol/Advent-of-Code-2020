

def part1(data):
    pos, dir = [0, 0], "E"
    dirs = {"N": (0, 1), "E": (1, 1), "S": (0, -1), "W": (1, -1)}
    d = list(dirs.keys())

    def move(pos, d, dist):
        pos[dirs[d][0]] += dirs[d][1] * dist
        return pos

    for line in data:
        if line[0] in dirs:
            pos = move(pos, line[0], int(line[1:]))
        elif line[0] == "L":
            dir = d[(d.index(dir) - int(int(line[1:])/90)) % len(d)]
        elif line[0] == "R":
            dir = d[(d.index(dir) + int(int(line[1:])/90)) % len(d)]
        elif line[0] == "F":
            pos = move(pos, dir, int(line[1:]))

    return abs(pos[0]) + abs(pos[1])


def part2(data):
    pos, wp = [0, 0], [1, 10]
    dirs = {"N": (0, 1), "E": (1, 1), "S": (0, -1), "W": (1, -1)}

    def move(pos, d, dist):
        pos[dirs[d][0]] += dirs[d][1] * dist
        return pos

    for line in data:
        if line[0] in dirs:
            wp = move(wp, line[0], int(line[1:]))
        elif line[0] in ["L", "R"]:
            for _ in range(int(int(line[1:])/90)):
                if line[0] == "L":
                    wp = [wp[1]+pos[0]-pos[1], pos[1]+pos[0]-wp[0]]
                else:
                    wp = [-wp[1]+pos[1]+pos[0], wp[0]-pos[0]+pos[1]]
        elif line[0] == "F":
            x, y = (wp[1] - pos[1]) * int(line[1:]), (wp[0] - pos[0]) * int(line[1:])
            pos, wp = [pos[0] + y, pos[1] + x], [wp[0] + y, wp[1] + x]

    return abs(pos[0]) + abs(pos[1])


data = open("day12.in").read().splitlines()
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


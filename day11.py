from itertools import product


def get_grid(data):
    return [list(row) for row in data]


def adj(p, dirs, grid, part=2):
    row, col = p
    set_occupied = 0

    for d in dirs:
        q = (row, col)
        while 0 <= q[0] + d[0] < len(grid) and 0 <= q[1] + d[1] < len(grid[0]):
            q = (q[0] + d[0], q[1] + d[1])
            if grid[q[0]][q[1]] in ["#", "L"]:
                if grid[q[0]][q[1]] == "#":
                    set_occupied += 1
                break
            if part == 1:
                break

    if grid[row][col] == "#":
        return "L" if set_occupied >= (4 if part == 1 else 5) else ""
    return "#" if set_occupied == 0 else ""


def run(data, part):
    grid = get_grid(data)
    dirs = [i for i in list(product([0, -1, +1], repeat=2)) if i != (0, 0)]

    while True:
        changes = set()
        occupied = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] in ["L", "#"]:
                    change = adj((row, col), dirs, grid, part=part)
                    if change:
                        changes.add(((row, col), change))
                    if grid[row][col] == "#":
                        occupied += 1
        if changes:
            for p in changes:
                grid[p[0][0]][p[0][1]] = p[1]
        else:
            return occupied


def part1(data):
    return run(data, part=1)

    
def part2(data):
    return run(data, part=2)



data = \
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".splitlines()


data = open("day11.in").read().splitlines()
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


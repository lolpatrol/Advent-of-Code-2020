

def get_graph(data):
    rows, cols = len(data), len(data[0])
    graph = [[char for char in row] for row in data]
    return graph, rows, cols


def part1(grid, rows, cols, slope=None):
    pos = [0, 0]

    if not slope:
        slope = [1, 3]

    tree_count = 0
    while pos[0] < rows - 1:
        pos = [pos[0] + slope[0], (pos[1] + slope[1]) % cols]
        if grid[pos[0]][pos[1]] == "#":
            tree_count += 1
    return tree_count
    
    
def part2(grid, rows, cols):
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    tree_count_prod = 1
    for slope in slopes:
        tree_count_prod *= part1(grid, rows, cols, slope)
    return tree_count_prod
    
    
data = open("day3.in").read().splitlines()
g, r, c = get_graph(data)

res1 = part1(g, r, c)
print("Part 1: ", res1)
    
res2 = part2(g, r, c)
print("Part 2: ", res2)


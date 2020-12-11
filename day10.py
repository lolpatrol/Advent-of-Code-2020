import numpy


def part1(data):
    data.sort()
    used, diff, jolts, rating = [], {1: 0, 3: 0}, 0, data[-1] + 3
    while True:
        valid = sorted([(i, abs(jolts - i)) for i in data if abs(jolts - i) <= 3 and i not in used])
        if not valid:
            diff[abs(jolts - rating)] += 1
            return diff[1] * diff[3]
        used.append(valid[0][0])
        diff[valid[0][1]] += 1
        jolts += valid[0][1]


def part2(data):
    data_map = {i: [] for i in [0] + data}
    for i in [0] + data:
        for j in [0] + data:
            if j > i and j - i <= 3:
                data_map[i].append(j)

    key_data = {list(data_map.keys())[i]: i for i in range(len(data_map.keys()))}

    adj = [[0 for _ in range(len(data) + 1)] for _ in range(len(data) + 1)]
    for i in key_data:
        for j in key_data:
            if j > i and j in data_map[i]:
                i_idx, j_idx = key_data[i], key_data[j]
                adj[i_idx][j_idx] = 1

    count = 0
    adj_ = adj = numpy.array(adj, dtype='int64')
    for i in range(len(data) + 1):
        adj = numpy.dot(adj, adj_)
        count += adj[0, len(adj[0])-1]

    return count


data = list(map(int, open("day10.in").read().splitlines()))
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


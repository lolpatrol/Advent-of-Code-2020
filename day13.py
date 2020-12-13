

def part1(data):
    time = int(data[0])
    buses = [int(i) for i in data[1].split(",") if i.isnumeric()]
    bus_wait_times = sorted([(bus, bus - (time % bus)) for bus in buses], key=lambda x: x[1])
    return bus_wait_times[0][0] * bus_wait_times[0][1]
    
    
def part2(data):
    # CRT
    buses = data[1].split(",")

    def minv(a, n):
        t, r, new_t, new_r = 0, n, 1, a
        while new_r != 0:
            q = int(r / new_r)
            t, new_t = new_t, t - q * new_t
            r, new_r = new_r, r - q * new_r
        if t < 0:
            t += n
        return t

    N, a_n = 1, []
    for i, bus in enumerate(buses):
        if bus.isnumeric():
            n = int(bus)
            a = -i % n
            N *= int(bus)
            a_n.append((a, n))

    y = [int(N / i[1]) for i in a_n]
    z = [minv(y[i], a_n[i][1]) % a_n[i][1] for i in range(len(a_n))]

    x = sum(a_n[i][0] * y[i] * z[i] for i in range(len(a_n)))

    return x % N
    
    
data = open("day13.in").read().splitlines()
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


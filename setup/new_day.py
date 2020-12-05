import sys


def make_day(day):
    day_str = \
f"""

def part1(data):
    return 0
    
    
def part2(data):
    return 0
    
    
data = open("day{day}.in").read()
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)

"""

    with open(f"day{day}.py", "w+") as f:
        f.write(day_str)

    with open(f"day{day}.in", "w+") as f:
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        day = sys.argv[1]
        make_day(day)
    else:
        print(f"Enter day as number. Received: {sys.argv}")
        sys.exit(0)


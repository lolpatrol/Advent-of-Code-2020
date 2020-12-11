

def parse_input(data):
    parsed = {}
    for line in data:
        l, r = [i[:-1] for i in line.split(" contain ")]
        parsed[l] = {}
        for item in r.split(", "):
            if not item[0].isnumeric():
                bag, num = 0, 0
            else:
                bag, num = item[2:], int(item[0])
                if num > 1:
                    bag = bag[:-1]
            parsed[l][bag] = num
    return parsed


def num_bags(bags, bag):
    return sum(bags[bag][b] + bags[bag][b] * num_bags(bags, b) for b in bags[bag]) if bag else 1


def has_gold(bags, bag):
    if 0 in bags[bag]:
        return {}
    has = {i for b in bags[bag] for i in has_gold(bags, b)}
    if has or "shiny gold bag" in bags[bag]:
        has.add(bag)
    return has


def part1(data):
    bags = parse_input(data)
    gold_bags = set()
    for bag in bags:
        gold_bags.update(has_gold(bags, bag))
    return len(gold_bags)


def part2(data):
    bags = parse_input(data)
    return num_bags(bags, "shiny gold bag")


data = open("day7.in").read().splitlines()
    
res1 = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


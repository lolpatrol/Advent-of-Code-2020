

def parse_input(data):
    passports = []
    for thing in data:
        fields = {
            "byr": None, "iyr": None, "eyr": None, "hgt": None,
            "hcl": None, "ecl": None, "pid": None, "cid": None
        }
        for line in thing.splitlines():
            l = line.split(" ")
            for item in l:
                fields[item.split(":")[0].strip()] = item.split(":")[1].strip()
        passports.append(fields)
    return passports


def part1(data):
    passports = parse_input(data)
    valid = []

    for p in passports:
        del p["cid"]
        count = sum([1 for k in p.keys() if p[k]])
        if count == len(p.keys()):
            valid.append(p)

    return len(valid)


def part2(data):
    valid = []
    passports = parse_input(data)

    for p in passports:
        if validate(p):
            valid.append(p)

    return len(valid)


def validate(entry):
    p = entry
    valid_count = 0

    if p["byr"] and 1920 <= int(p["byr"]) <= 2002:
        valid_count += 1

    if p["iyr"] and 2010 <= int(p["iyr"]) <= 2020:
        valid_count += 1

    if p["eyr"] and 2020 <= int(p["eyr"]) <= 2030:
        valid_count += 1

    if p["hgt"]:
        if ("cm" in p["hgt"] and 150 <= int(p["hgt"][:-2]) <= 193) or ("in" in p["hgt"] and 59 <= int(p["hgt"][:-2]) <= 76):
            valid_count += 1

    if p["hcl"] and p["hcl"][0] == "#" and len(p["hcl"][1:]) == 6:
        valid_count += 1 if sum(1 for i in p["hcl"][1:] if i in "0123456789abcdef") == 6 else 0

    if p["ecl"] and p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        valid_count += 1

    if p["pid"] and len(p["pid"]) == 9:
        valid_count += 1

    return valid_count == 7


data = open("day4.in").read().split("\n\n")

res1 = part1(data)
print("Part 1: ", res1)

res2 = part2(data)
print("Part 2: ", res2)


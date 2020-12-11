

def part1(data):
    ptr, acc = 0, 0
    done = set()
    while ptr < len(data):
        next_ptr, next_acc = op(data[ptr], acc, ptr)
        if (data[ptr], ptr) in done:
            return acc, ptr >= len(data)
        done.add((data[ptr], ptr))
        ptr, acc = next_ptr, next_acc
    return acc, ptr >= len(data)

    
def part2(data):
    mod = lambda x: f"{dict({'jmp': 'nop', 'nop': 'jmp'})[x[:3]]}{x[3:]}"
    mod_data = [(i, mod(data[i])) for i in range(len(data)) if data[i][:3] in ["jmp", "nop"]]
    for i, ins in mod_data:
        res, finished = part1(data[:i] + [ins] + data[i+1:])
        if finished:
            return res


def op(ins, accumulator, pointer):
    instruction, var = ins.split(" ")

    sign, val = var[0], int(var[1:])
    if sign == "-":
        val = -val

    if instruction == "acc":
        accumulator += val
    elif instruction == "jmp":
        pointer += val - 1

    return pointer + 1, accumulator


data = open("day8.in").read().splitlines()

res1, _ = part1(data)
print("Part 1: ", res1)
    
res2 = part2(data)
print("Part 2: ", res2)


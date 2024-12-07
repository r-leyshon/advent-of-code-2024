import itertools

from pyprojroot import here

from aoc.utils.io import load_input


def munge_data(dat:list) -> dict:
    out = dict()
    for line in dat:
        split_line = line.split(":")
        key = int(split_line[0])
        nums = [ int(i) for i in split_line[-1].split(" ") if i != ""]
        out[key] = nums
    return out


def evaluate_expressions(nums:list, ops:itertools.product):
    out = nums[0]
    for i, op in enumerate(ops):
        if op == "+":
            out += nums[i + 1]
        elif op == "*":
            out *= nums[i + 1]
        elif op == "|":
            repl = str(out) + str(nums[i + 1])
            out = int(repl)
    return out


def solve_both(_input:dict, _operators:str = "+*"):
    true_vals = list()
    for key, vals in _input.items():
        op_combos = itertools.product(_operators, repeat=len(vals) - 1)
        for operators in op_combos:
            if evaluate_expressions(nums=vals, ops=operators) == key:
                true_vals.append(key)
                break # only need to know that one value is correct
            else:
                continue
    return sum(true_vals)


def solve():
    example_dat = load_input(here("07-bridge-repair/example.txt"))
    print("Part One")
    print(f"Answer to example is {solve_both(munge_data(example_dat))}")
    input_dat = load_input(here("07-bridge-repair/input.txt"))
    print(f"Answer to part one is {solve_both(munge_data(input_dat))}")
    print("Part Two")
    print(f"Answer to example is {solve_both(munge_data(example_dat), '+|*')}")
    print(f"Answer to part two is {solve_both(munge_data(input_dat), '+|*')}")


if __name__ == "__main__":
    solve()
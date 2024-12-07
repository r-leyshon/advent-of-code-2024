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
    return out


def solve_part_one(_input:dict):
    true_vals = list()
    for key, vals in _input.items():
        op_combos = itertools.product("+*", repeat=len(vals) - 1)
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
    print(f"Answer to example is {solve_part_one(munge_data(example_dat))}")

if __name__ == "__main__":
    solve()
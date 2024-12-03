import re

from pyprojroot import here

from aoc.utils.io import load_input


def munge_data(_input:list) -> list:
    mul_pat = re.compile(r"mul\(\d+,\d+\)")
    hits = mul_pat.findall("".join(_input))
    statements = []
    for pat in hits:
        nums = pat.replace("mul(", "").replace(")", "").split(",")
        nums = [int(i) for i in nums]
        statements.append(nums)
    return statements


def calc_results(statements:list) -> int:
    return sum((case[0] * case[1] for case in statements))


def get_answers():
    example_pth = here("03-mull-it-over/example.txt")
    example = calc_results(munge_data(load_input(example_pth)))
    input_pth = here("03-mull-it-over/input.txt")
    _input = calc_results(munge_data(load_input(input_pth)))
    print("Part one")
    print(f"The answer to the example is {example}")
    print(f"The answer to the input is {_input}")


if __name__ == "__main__":
    get_answers()
                                 
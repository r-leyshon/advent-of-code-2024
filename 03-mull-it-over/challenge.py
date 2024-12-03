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


def redact_puzzle(_input:list) -> list:
    compiled_puz = "".join(_input)
    dont_pat = re.compile(r"don't\(\).*?do\(\)")
    hits = dont_pat.findall(compiled_puz)
    puz_out = compiled_puz
    for i in hits:
        puz_out = puz_out.replace(i, "")
    return puz_out


def get_answers():
    example_pth = here("03-mull-it-over/example.txt")
    example = calc_results(munge_data(load_input(example_pth)))
    input_pth = here("03-mull-it-over/input.txt")
    loaded_input = load_input(input_pth)
    _input = calc_results(munge_data(loaded_input))
    print("Part one")
    print(f"The answer to the example is {example}")
    print(f"The answer to the input is {_input}")

    example2_pth = here("03-mull-it-over/example2.txt")
    example2 = load_input(example2_pth)
    redacted_example = redact_puzzle(example2)
    example2_out = calc_results(munge_data(redacted_example))
    redacted_input = redact_puzzle(loaded_input)
    input2_out = calc_results(munge_data(redacted_input))
    print("Part two")
    print(f"The answer to the example is {example2_out}")
    print(f"The answer to the input is {input2_out}")


if __name__ == "__main__":
    get_answers()
                                 
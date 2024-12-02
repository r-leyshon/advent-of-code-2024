from pyprojroot import here

from aoc.utils.io import load_input


def munge_data(_in:list) -> list:
    # split on space
    _in = [i.split(" ") for i in _in]
    _out = list()
    # convert to int
    for i in _in:
        listed_ints = [int(j) for j in i]
        _out.append(listed_ints)
    return _out


def check_direction(report:list) -> str:
    # compare first & second items to get direction
    num_lvls = len(report)
    i = 0
    while i < num_lvls:
        if report[i] > report[i + 1]:
            return "down"
        elif report[i] < report[i + 1]:
            return "up"
        elif report[i] == report[i + 1]:
            # if there's no diff, check the next 2 items
            i += 1
        elif i == num_lvls:
            # check the input doesn't throw a wobbly
            raise Exception("Out of range")


def is_diff_safe(num1:int, num2:int, _dir:str) -> bool:
    if _dir == "down":
        diff = num1 - num2
    elif _dir == "up":
        diff = num2 - num1
    SAFE_VALS = [1, 2, 3]
    if diff in SAFE_VALS:
        return True # safe
    else:
        return False # unsafe


def is_report_safe(report:list) -> bool:
    _dir = check_direction(report)
    num_lvls = len(report)
    i = 0
    is_safe = True
    while i < (num_lvls - 1):
        if not is_diff_safe(report[i], report[i + 1], _dir):
            is_safe = False
        i += 1
    return is_safe


# part 1 ==================================================================


def answers():
    example_pth = here("02-red-nosed-reports/example.txt")
    example = load_input(example_pth)
    example_dat = munge_data(example)

    input_pth = here("02-red-nosed-reports/input.txt")
    _input = load_input(input_pth)
    input_dat = munge_data(_input)
    eg_outcomes = [is_report_safe(report) for report in example_dat]
    outcomes = [is_report_safe(report) for report in input_dat]

    print(f"There are {sum(eg_outcomes)} safe reports in the example")
    print(f"There are {sum(outcomes)} safe reports in the input")


if __name__ == "__main__":
    answers()

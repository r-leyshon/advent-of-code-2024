import argparse
import logging
from pyprojroot import here

from aoc.utils.io import load_input

# Set up argument parser
parser = argparse.ArgumentParser(description="Red Nosed Reports")
parser.add_argument(
    "--LOGGING", action="store_true", help="Enable logging to a file")
args = parser.parse_args()

if args.LOGGING:
    # Configure logging
    logging.basicConfig(
        filename=here("02-red-nosed-reports/output.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )


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


def is_report_safe(
    report:list, problem_dampener:bool=False, logz:bool=args.LOGGING
    ) -> bool:
    local_report = report.copy()
    _dir = check_direction(local_report)
    num_lvls = len(local_report)
    i = 0
    is_safe = True
    if logz:
        logging.info(f"Examining report {local_report}")
        logging.info(f"direction is {_dir}")

    while i < (num_lvls - 1):
        if logz:
            logging.info(f"Problem dampener is {problem_dampener}")
            logging.info(
                f"Comparing {local_report[i]} and {local_report[i + 1]}")
        if not is_diff_safe(local_report[i], local_report[i + 1], _dir):
            if problem_dampener:
                # you need to decide which index to drop, for example:
                # [82, 84, 85, 87, 90, 92, 91], problem is 90, 92, 91,
                # dropping first problem index (92) won't fix the issue
                diff = is_diff_safe(
                    local_report[i - 1], local_report[i], _dir)                
                if diff:
                    prob_ind = i + 1
                else:
                    prob_ind = i    
                del local_report[prob_ind]
                num_lvls = len(local_report)
                # don't do this again
                problem_dampener = False
                if logz:
                    logging.info(
                        f"Deleting index {i} value {local_report[i]}")
                    logging.info(
                        f"Examining updated report {local_report}")
                    logging.info("Starting from scratch")
                # start from scratch
                i = 0
                continue
            else:
                is_safe = False
                break
        i += 1
    if logz:
        logging.info(f"Report {report } outcome is safe: {is_safe}")
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
    print("Part 1: Unsafe reports")
    print(f"There are {sum(eg_outcomes)} safe reports in the example")
    print(f"There are {sum(outcomes)} safe reports in the input")

    eg_outcomes = [
        is_report_safe(report, problem_dampener=True) for report in example_dat]
    outcomes = [
        is_report_safe(report, problem_dampener=True) for report in input_dat]
    print("Part 2: Unsafe reports with problem dampener")
    print(f"There are {sum(eg_outcomes)} safe reports in the example")
    print(f"There are {sum(outcomes)} safe reports in the input")
    

if __name__ == "__main__":
    answers()

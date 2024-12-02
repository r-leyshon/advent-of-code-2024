"""Run with `python3 -m 01-hystorian-hysteria.challenge`"""
from pyprojroot import here

from aoc.utils.io import load_input

# func 1: munge data =====================================================


def munge_input(_in:list) -> tuple:
    # split the numbers on space
    two_lists = (list(), list())
    for i in _in:
        nums = tuple(j for j in i.split(" ") if j != "")
        # cast to ints
        nums = tuple(int(j) for j in nums)
        # assign 1st and 2nd to independent lists
        two_lists[0].append(nums[0])
        two_lists[1].append(nums[1])
    # sort those lists
    return tuple(sorted(_li) for _li in two_lists)


# func 2: sum the diffs ===================================================


def sum_diffs(_lists:tuple) -> int:    
    # zip both lists
    paired = zip(_lists[0], _lists[1])
    # iterate & calculate the diffs
    diffs = [abs(i[0] - i[1]) for i in paired]
    # sum the diffs 
    return sum(diffs)



# part 2: similarity score ================================================


def similarity(_lists):
    sims = list()
    for i in _lists[0]:
        _count = 0
        for j in _lists[1]:
            if i == j:
                _count += 1
        sims.append(i * _count)
    return sum(sims)


def answers():
    example_pth = here("01-hystorian-hysteria/example.txt")
    input_pth = here("01-hystorian-hysteria/input.txt")
    example = load_input(example_pth)
    challenge = load_input(input_pth)
    print(f"Part one example is {sum_diffs(munge_input(example))}")
    print(f"Part one solution is: {sum_diffs(munge_input(challenge))}")
    print(f"Part two example is {similarity(munge_input(example))}")
    print(f"Part two solution is: {similarity(munge_input(challenge))}")

if __name__ == "__main__":
    answers()

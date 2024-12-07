from pyprojroot import here

from aoc.utils.io import load_input

example_pth = here("05-print-queue/example.txt")

example_dat = load_input(example_pth)


# munge data

# page order rules and updates are separated by ""

sep = example_dat.index("")
order = example_dat[0:sep]
updates = example_dat[sep + 1:]




ups = updates[0].split(",")

# return only the order rules that are relevant to this update
for i, num in enumerate(ups):
    nums_to_right = ups[i+1:]

    relevant_rules = []
    # lets get rules including i and i to the right only
    for j in order:
        include = False
        for k in nums_to_right:
            # print(f"k:{k} vs j:{j}")
            if k in j:
                include = True

        # print(f"Include: {include}")

        if num in j:
            relevant_rules.append(j)
    print(num)
    print(relevant_rules)


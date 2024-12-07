from pyprojroot import here

from aoc.utils.io import load_input


example_pth = here("04-ceres-search/example.txt")

example_dat = load_input(example_pth)

puz = example_dat

def search_for_str(puz:list, _str:str="XMAS"):
    rev_str = _str[::-1]
    _str_len = len(_str)
    puz_len = len(puz)
    search_ind = 0 # use this to sequence through the string
    _str_count = 0
    # find indexes of string sequence
    for i, row in enumerate(puz):
        for j, letter in enumerate(row):


            if _str[search_ind] == letter:
                # search around for next letter in _str
                # index errors mean hitting the edge of the puzzle, so try except them

                try:

                    # line search ind + 1
                    if row[j:j+4] == "XMAS":
                        print("Caught a straightforward case")
                    
                    # line search ind - 1
                    if row[j-3:j+1] == "SAMX":
                        print("Caught a backwards case")
                    

                    # row search - 1, line search ind - 1, ind, ind +1
                    # row search + 1, line search ind - 1, ind, ind +1
                    # this can't be an either or scenario, must search all available options
                    # up 
                    if "".join([line[j] for line in puz[i-3:i+1]]) == "SAMX":
                        print("Caught an upwards case")
                    # down
                    if "".join([line[j] for line in puz[i:i+4]]) == "XMAS":
                        print("Caught a downwards case")
                    

                    # diag 1 o'clock
                    # ...



                except IndexError:
                    # do not increment _str_count, edge of puzzle encountered
                    continue


# chained if statement searches surrounding indices for next letter












import re
import time

from pyprojroot import here

from aoc.utils.io import load_input

example_pth = here("06-guard-gallivant/example.txt")
example_dat = load_input(example_pth)


class PuzzleHandler:


    def __init__(self, puzzle_pth:list):
        self.puz = load_input(puzzle_pth)
        self.ORIENTATIONS = ["^", ">", "v", "<"]
        self.next_step = "."
        self.curr_loc = (0,0)
        self.next_loc = (0,0)
        self.curr_orient = "^"


    def find_guard(self) -> tuple:
        """Returns the row, column index and orientation of the guard"""
        guard_pat = re.compile(r"\^|>|v|<")
        for i, row in enumerate(self.puz):
            hit = guard_pat.search(row)
            if hit:
                j = hit.span()[0]
                self.curr_loc = (i, j)
                self.curr_orient = hit.group()
                return (i, j, hit.group())
            else:
                continue


    def _replace_at_index(self, s, index, replacement):
        # utility for adjusting string at a specified index
        s_list = list(s)
        s_list[index] = replacement
        return ''.join(s_list)


    def move_guard(
        self,
        puz:list,
        curr_loc:tuple,
        next_loc:tuple,
        curr_orient:str) -> list:
        """Update the guard position in the puzzle"""
        print(f"Moving guard from {curr_loc} to {next_loc}")
        local_puz = puz.copy()
        local_puz[next_loc[0]] = self._replace_at_index(
            local_puz[next_loc[0]], next_loc[1], curr_orient)
        # replace current location with an "X"
        local_puz[curr_loc[0]] = self._replace_at_index(
            local_puz[curr_loc[0]], curr_loc[1], "X")
        print(f"Guard has moved, row is now: {local_puz[curr_loc[0]]}")
        return local_puz


    def turn_guard(self):
        print(f"Adjusting current orientation: {self.curr_orient}")
        orient_ind = self.ORIENTATIONS.index(self.curr_orient)
        try:
            new_orient = self.ORIENTATIONS[orient_ind + 1]
        except IndexError:
            # in case where the last ORIENTATION "<" is current
            new_orient = self.ORIENTATIONS[0]
        self.curr_orient = new_orient
        print(f"New orientation: {self.curr_orient}")
        return new_orient


    def move_upwards(self) -> tuple:
        print("Going upwards...")
        local_puz = self.move_guard(
            self.puz,
            curr_loc=self.curr_loc,
            next_loc=self.next_loc,
            curr_orient=self.curr_orient
            )
        self.puz = local_puz
        self.next_loc = (self.next_loc[0] - 1, self.next_loc[1])
        self.curr_loc = (self.curr_loc[0] - 1, self.curr_loc[1])
        return (self.curr_loc, self.next_loc)


    def move_right(self) -> tuple:
        print("Going right...")
        local_puz = self.move_guard(
            self.puz,
            curr_loc=self.curr_loc,
            next_loc=self.next_loc,
            curr_orient=self.curr_orient
            )
        self.puz = local_puz
        self.next_loc = (self.next_loc[0] - 1, self.next_loc[1])
        self.curr_loc = (self.curr_loc[0] - 1, self.curr_loc[1])
        return (self.curr_loc, self.next_loc)


    def move_down(self) -> tuple:
        print("Going down...")
        local_puz = self.move_guard(
            self.puz,
            curr_loc=self.curr_loc,
            next_loc=self.next_loc,
            curr_orient=self.curr_orient
            )
        self.puz = local_puz
        self.next_loc = (self.next_loc[0] - 1, self.next_loc[1])
        self.curr_loc = (self.curr_loc[0] - 1, self.curr_loc[1])
        return (self.curr_loc, self.next_loc)


    def move_left(self) -> tuple:
        print("Going left...")
        local_puz = self.move_guard(
            self.puz,
            curr_loc=self.curr_loc,
            next_loc=self.next_loc,
            curr_orient=self.curr_orient
            )
        self.puz = local_puz
        self.next_loc = (self.next_loc[0] - 1, self.next_loc[1])
        self.curr_loc = (self.curr_loc[0] - 1, self.curr_loc[1])
        return (self.curr_loc, self.next_loc)
    

    def solve_puzzle(self) -> int:
        curr_row = self.curr_loc[0]
        curr_col = self.curr_loc[1]
        
        while (curr_row >= 0) and (curr_col <= len(self.puz[curr_row]) - 1) :
            print(f"current row: {curr_row}, current column: {curr_col}")
            print(f"Next step is a {self.next_step}")

            if self.next_step != "#":

                # if orientation is ^, look at col index at previous row
                if self.curr_orient == self.ORIENTATIONS[0]:

                    self.next_loc = (
                        # decrease row, col constant
                        self.curr_loc[0] - 1, self.curr_loc[1]
                        )
                    print(f"Next location is {self.next_loc}")
                    self.next_step = self.puz[self.next_loc[0]][self.next_loc[1]]
                    self.move_upwards()
                    print(f"Updated current location: {self.curr_loc}")
                    # update local vars
                    curr_row, curr_col = self.curr_loc
                    continue

                elif self.curr_orient == self.ORIENTATIONS[1]:

                    self.next_loc = (
                        # constant row, increase col
                        self.curr_loc[0], self.curr_loc[1] + 1
                        )
                    print(f"Next location is {self.next_loc}")
                    self.next_step = self.puz[self.next_loc[0]][self.next_loc[1]]
                    print(f"next step is: {self.next_step}")

                    self.move_right()
                    print(f"Updated current location: {self.curr_loc}")
                    # update local vars
                    curr_row, curr_col = self.curr_loc
                    continue
                elif self.curr_orient == self.ORIENTATIONS[2]:

                    self.next_loc = (
                        # increase row, col constant
                        self.curr_loc[0] + 1, self.curr_loc[1]
                        )
                    print(f"Next location is {self.next_loc}")
                    self.next_step = self.puz[self.next_loc[0]][self.next_loc[1]]
                    print(f"next step is: {self.next_step}")

                    self.move_down()
                    print(f"Updated current location: {self.curr_loc}")
                    # update local vars
                    curr_row, curr_col = self.curr_loc
                    continue
                elif self.curr_orient == self.ORIENTATIONS[3]:

                    self.next_loc = (
                        # constant row, decrease col
                        self.curr_loc[0], self.curr_loc[1] - 1
                        )
                    print(f"Next location is {self.next_loc}")
                    self.next_step = self.puz[self.next_loc[0]][self.next_loc[1]]
                    print(f"next step is: {self.next_step}")

                    self.move_left()
                    print(f"Updated current location: {self.curr_loc}")
                    # update local vars
                    curr_row, curr_col = self.curr_loc
                    continue

            else:
                self.turn_guard()
                print(f"Adjusted orientation{self.curr_orient}")
                # update current guard location with the new orientation
                print(f"Current location is: {self.curr_loc}")
                print(f"row to update is: {self.puz[self.curr_loc[0]]}")
                self.puz[self.curr_loc[0]] = self._replace_at_index(
                    self.puz[self.curr_loc[0]],
                    self.curr_loc[1],
                    self.curr_orient
                    )
                break
                

        return self.puz


puzzle_handler = PuzzleHandler(puzzle_pth=example_pth)
puzzle_handler.find_guard()
current_row, current_col = puzzle_handler.curr_loc
current_orientation = puzzle_handler.curr_orient

puzzle_handler.solve_puzzle()


puzzle_handler.puz






# break
# # if not blocked, replace ^ with X in current row
# # Replace . or X in next step with current orientation


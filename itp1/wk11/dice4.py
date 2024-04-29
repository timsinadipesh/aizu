"""
reads n dices
determines whether they are all different
"""

import sys

class Dice:
    def __init__(self, assigned_nums):
        self.positions = assigned_nums

    def rotate(self, new_positions_idx):
        new_positions = []
        for i in range(6):
            new_positions.append(self.positions[new_positions_idx[i]])
        return new_positions

    def eastward(self):
        self.positions = self.rotate([3, 1, 0, 5, 4, 2])

    def westward(self):
        self.positions = self.rotate([2, 1, 5, 0, 4, 3])

    def northward(self):
        self.positions = self.rotate([1, 5, 2, 3, 0, 4])

    def southward(self):
        self.positions = self.rotate([4, 0, 2, 3, 5, 1])

    def turn_in_place(self):
        self.positions = self.rotate([0, 2, 4, 1, 3, 5])

    def find_top_position(self, top):
        # look for the top in the south direction thrice
        for i in range(3):
            self.southward()
            if self.positions[0] == top:
                return
        # look for the top in the east direction thrice
        for i in range(3):
            self.eastward()
            if self.positions[0] == top:
                return

    def find_top_front_position(self, top, front):
        if self.positions[0] != top:       # look for the top position only if it is not already there 
            self.find_top_position(top)   
        for i in range(4):       # if any of the 4 sides matches the target front
            if self.positions[1] == front:
                return True
            self.turn_in_place()
        return False

    def find_match(self, other):
        for direction in ["e", "n"]:
            for i in range(3):
                # match top and front of one dice with the other
                top1, front1 = other.positions[0], other.positions[1]       
                top_front_matched = self.find_top_front_position(top1, front1)

                if top_front_matched and other.positions == self.positions:
                    print("No")
                    sys.exit(0)     # match found, stop execution
                
                if direction == "e":
                    other.eastward()
                elif direction == "n":
                    other.northward()

# read the assigned numbers from the cli and make dices
n = int(input())
dices = []
for i in range(n):
    assigned_nums = list(map(int, input().split()))
    dices.append(Dice(assigned_nums))               # make dices

for i in range(n):              # compare each dice
    for j in range(i + 1, n):   # with new dices that have not been compared yet
        dices[i].find_match(dices[j])   # keep on looking for a match

print("Yes")       # all dices are different

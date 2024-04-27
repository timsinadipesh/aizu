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

# read the assigned numbers from the cli and make dices
dice1_nums = list(map(int, input().split()))
dice2_nums = list(map(int, input().split()))
dice1 = Dice(dice1_nums)
dice2 = Dice(dice2_nums)

def match_print(dice1, dice2):
    # match top and front of one dice with the other
    top1, front1 = dice1.positions[0], dice1.positions[1]
    match_2_dices = dice2.find_top_front_position(top1, front1)

    print(dice1.positions)
    print(dice2.positions)
    print()

    if match_2_dices and dice1.positions == dice2.positions:
        print("Yes")
        sys.exit(0)

match_print(dice1, dice2)
for i in range(3):
    dice2.eastward()
    match_print(dice1, dice2)
for i in range(3):
    dice2.northward()
    match_print(dice1, dice2)

print("No")
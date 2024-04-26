"""
dice construction is the same as in dice1.py

now, the numbers on the top face and front face are given
prints the number on the right side face
"""

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

        if self.positions[1] == front:     # the front has the target front number
            print(self.positions[2])
        if self.positions[2] == front:     # look to the right of the top
            print(self.positions[4])
        elif self.positions[3] == front:   # look to the left of the top
            print(self.positions[1])
        elif self.positions[4] == front:   # look to the back of the top
            print(self.positions[3])


assigned_nums = list(map(int, input().split()))
q = int(input())

dice = Dice(assigned_nums)
print("dice.positions:", dice.positions,"\n")

for i in range(q):
    top, front = list(map(int, input().split()))
    dice.find_top_front_position(top, front)
    print("dice position:", dice.positions)
    print()
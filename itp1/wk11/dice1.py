"""
rolling dice simulation

reads numbers asssigned to each face
and a sequence of commands to roll the dice
prints the number on the top face
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

assigned_nums = list(map(int, input().split()))
commands = input()

dice = Dice(assigned_nums)

for command in commands:
    if command == 'E': dice.eastward()
    elif command == 'W': dice.westward()
    elif command == 'N': dice.northward()
    elif command == 'S': dice.southward()

print(dice.positions[0])
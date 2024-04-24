"""
rolling dice simulation

reads integers asssigned to each face
and a sequence of commands to roll the dice
prints the integer on the top face
"""

class Dice:
    def __init__(self):
        self.positions = [1, 2, 3, 4, 5, 6]

    def eastward(self):
        new_positions = [0] * 6
        new_positions[0] = self.positions[3]
        new_positions[1] = self.positions[1]
        new_positions[2] = self.positions[0]
        new_positions[3] = self.positions[5]
        new_positions[4] = self.positions[4]
        new_positions[5] = self.positions[2]
        self.positions = new_positions

    def westward(self):
        new_positions = [0] * 6
        new_positions[0] = self.positions[2]
        new_positions[1] = self.positions[1]
        new_positions[2] = self.positions[5]
        new_positions[3] = self.positions[0]
        new_positions[4] = self.positions[4]
        new_positions[5] = self.positions[3]
        self.positions = new_positions

    def northward(self):
        new_positions = [0] * 6
        new_positions[0] = self.positions[1]
        new_positions[1] = self.positions[5]
        new_positions[2] = self.positions[2]
        new_positions[3] = self.positions[3]
        new_positions[4] = self.positions[0]
        new_positions[5] = self.positions[4]
        self.positions = new_positions

    def southward(self):
        new_positions = [0] * 6
        new_positions[0] = self.positions[4]
        new_positions[1] = self.positions[0]
        new_positions[2] = self.positions[2]
        new_positions[3] = self.positions[3]
        new_positions[4] = self.positions[5]
        new_positions[5] = self.positions[1]
        self.positions = new_positions

assigned_ints = list(map(int, input().split()))
commands = input()

dice = Dice()

for command in commands:
    if command == 'E': dice.eastward()
    elif command == 'W': dice.westward()
    elif command == 'N': dice.northward()
    elif command == 'S': dice.southward()

print(assigned_ints[dice.positions[0] - 1])
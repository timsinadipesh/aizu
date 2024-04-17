"""
Using a stack to calculate an expresssion
in the reverse polish notation
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    

input_items = input().split(" ")
nums = Stack()
result = 0

for each in input_items:
    if each.isdigit():
        nums.push(int(each))
    else:
        num1 = nums.pop()
        num2 = nums.pop() if nums.stack else 0

        if each == '+':
            result = num1 + num2
        elif each == '-':
            result = num2 - num1
        elif each == '*':
            result = num1 * num2
        
        nums.push(result)

print(nums.stack[-1])

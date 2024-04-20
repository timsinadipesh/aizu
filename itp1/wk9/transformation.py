"""
performs a sequence of commands to a given string st

replace i j rep: replace from i-th char to j-th char
                 of st with rep
reverse i j: reverse from i-th char to j-th char of st
print i j: print from i-th char to j-th char of st
"""

def replace(uin, i, j, rep):
    return uin[:i] + rep + uin[j+1:]

def reverse_st(uin, i, j):
    return uin[:i] + uin[i:j+1][::-1] + uin[j+1:]

def print_slice(uin, i, j):
    return uin[i:j+1]

st = input()

q = int(input())

for i in range(q):
    line = input().split()
    op, i, j = line[0], int(line[1]), int(line[2])

    if op == "replace":
        st = replace(st, i, j, line[3])
    elif op == "reverse":
        st = reverse_st(st, i, j)
    elif op == "print":
        print(print_slice(st, i, j))

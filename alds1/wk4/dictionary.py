"""
a simple dictionary program
can insert a string in to the dictionary
searches for the string, prints 'yes' if found
and 'no' otherwise
"""

ops = int(input())

di = {}

for _ in range(ops):
    op, st = input().split(" ")
    fst_char = st[0]

    if op == "insert":
        if fst_char in di.keys():
            if st not in di[fst_char]:
                di[fst_char].add(st)
        else:
            di[fst_char] = set()
            di[fst_char].add(st)
    elif op == "find":
        if fst_char in di.keys():
            if st in di[fst_char]:
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        sys.exit(-1)
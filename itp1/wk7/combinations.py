"""
takes two integer input n and x separated by a comma
terminates when both integers are 0

the program finds 3 unique digits from 1 to n whose sum equals x
"""
import sys

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        sys.exit()  

    ways = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    ways += 1
    print(ways)
"""
reads a n * m matrix A and a m * l matrix B
and prints their product, a n * l matrix C
"""

n, m, l = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(m):
    b.append(list(map(int, input().split())))


for i in range(n):
    res = []
    for j in range(l):
        total = 0
        for k in range(m):
            total += a[i][k] * b[k][j]
        res.append(total)
    for idx, val in enumerate(res):
        print(val, end=" " if idx != len(res) - 1 else "\n")
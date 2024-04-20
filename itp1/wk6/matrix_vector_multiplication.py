"""
reads a n * m matrix A and a m * 1 vector b
and prints their product Ab
"""

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(m):
    b.append(int(input()))

for i in range(n):
    total = 0
    for j in range(m):
        total += a[i][j] * b[j]
    print(total)
      
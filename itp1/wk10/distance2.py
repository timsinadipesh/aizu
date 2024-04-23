"""
reads two n dimensional vectors; x and y
calculates minkowski's distance where p = 1,2,3,inf
"""

n = int(input()) # length of the vectors

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_y = [abs(x[i] - y[i]) for i in range(n)]
print(sum(x_y))             # p = 1, or manhattan distance

x_y_2 = [x**2 for x in x_y]
print((sum(x_y_2))**(1/2))  # p = 2, or euclidean distance

x_y_3 = [x**3 for x in x_y]
print((sum(x_y_3)**(1/3)))  # p = 3

print(max(x_y))             # chebyshev distance


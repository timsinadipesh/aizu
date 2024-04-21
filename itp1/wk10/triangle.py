"""
two sides of a triangle a and b
and the angle C between them are given in a line

calculate:
S: area of the triangle
L: length of the circumference of the triangle
h: height of the triangle with side b as a bottom edge
"""

import math

# side a, side b, angle C
a, b, C_deg = map(int, input().split())

C = math.radians(C_deg)

# area of the triange
S = 1/2 * a * b * math.sin(C)

# third side
c = math.sqrt(a**2 + b**2 - (2 * a * b * math.cos(C)))

# length of the circumference of the triangle
L = a + b + c

# height of the triangle with side b as a bottom edge
h = b * math.sin(C)

print(round(S, 6))
print(round(L, 6))
print(round(h, 6))
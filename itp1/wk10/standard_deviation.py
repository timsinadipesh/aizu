"""
takes final scores of an examination for n students and
calculates standard deviation of the scores s1, s2, ..., sn
"""

import sys
import math

while True:
    n = int(input())
    if n == 0:
        sys.exit(0)

    scores = list(map(int, input().split()))
    m = sum(scores) / n               # mean
    var = 0
    for i in range(n):
        var += (scores[i] - m)**2
    var /= n                          # variance
    sd = math.sqrt(var)               # standard deviation
    print(sd)
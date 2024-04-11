# using the euclidean algorithm to find the greatest common divisor

a, b = map(int, input().split(" "))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(a, b))

import math

def product( s, n):
    numberator = 1
    denominator = 1
    for i in range(0,n):
        # nu = int(input())
        # de = int
        numberator *= s[i][0]
        denominator *= s[i][1]
    return numberator, denominator
def irreducible(a , b ):
    x = math.gcd(a , b)
    a = a // x
    b = b // x
    return a, b

n = int(input())
s = []
for i in range(0,n):
    ab = list(map(int, input().split()))
    s.append(ab)
numberator, denominator = product(s,n)
numberator, denominator = irreducible(a = numberator, b = denominator)

print(numberator,denominator)
# 최대공약수와 최소공배수
import sys
from math import gcd
input = sys.stdin.readline

def lcm(x, y):
    return x * y // gcd(x, y)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))

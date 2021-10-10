# 최소공배수
import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = a*b // math.gcd(a, b)
    print(ans)

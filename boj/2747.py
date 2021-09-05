# 피보나치 수

import sys

input = sys.stdin.readline

p = [0, 1]
n = int(input())

for i in range(1, n+1):
    p.append(p[i-1]+p[i])

print(p[n])

# 피보나치 수 2
import sys
input = sys.stdin.readline

p = [0, 1]
n = int(input())

for i in range(n-1):
    a = p[i] + p[i+1]
    p.append(a)

print(p[n])

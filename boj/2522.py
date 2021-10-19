# 별 찍기 - 12
import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n):
    print(" "*(n-i) + "*"*i)
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*i)

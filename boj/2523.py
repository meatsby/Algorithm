# 별 찍기 - 13
import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n):
    print("*"*i)
for i in range(n, 0, -1):
    print("*"*i)

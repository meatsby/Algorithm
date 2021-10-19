# 별 찍기 - 6
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(i+(i-1)))

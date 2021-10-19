# 별 찍기 - 16
import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + " ".join(["*"]*i))

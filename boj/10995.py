# 별 찍기 - 20
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(" "*(i%2) + " ".join(["*"]*n))

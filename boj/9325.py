# 얼마?
import sys
input = sys.stdin.readline

for t in range(int(input())):
    s = int(input())
    for n in range(int(input())):
        q, p = map(int, input().split())
        s += q*p
    print(s)

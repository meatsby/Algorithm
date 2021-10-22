# 대회 자리
import sys
input = sys.stdin.readline

for k in range(int(input())):
    p, m = map(int, input().split())
    seats = [0 for _ in range(m+1)]
    cant = 0
    for i in range(p):
        s = int(input())
        if seats[s] == 0:
            seats[s] = 1
        else:
            cant += 1
    print(cant)

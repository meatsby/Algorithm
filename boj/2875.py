# 대회 or 인턴

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
team = min(N//2, M)
f = N - team*2
m = M - team
left = f + m
need = K - left

if need <= 0:
    print(team)
else:
    print((team*3 - need)//3)

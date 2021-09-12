# 올림픽

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
olym = [list(map(int, input().split())) for _ in range(n)]
olym.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if olym[i][0] == k:
        myscore = olym[i][1:]

rank = 1

for i in range(n):
    if olym[i][1:] == myscore:
        break
    rank += 1

print(rank)

# 세로읽기

import sys

input = sys.stdin.readline

ml = 0
alp = []

for _ in range(5):
    l = list(input().rstrip())
    alp.append(l)
    ml = max(ml, len(l))

for j in range(ml):
    for i in range(5):
        try:
            print(alp[i][j], end="")
        except IndexError:
            continue

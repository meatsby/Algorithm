# 상하좌우

import sys

input = sys.stdin.readline

n = int(input())
move = list(input().split())

x, y = 1, 1
mv = ["R", "L", "D", "U"]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for m in move:
    nx = x + dx[mv.index(m)]
    ny = y + dy[mv.index(m)]
    if 0 < nx <= n and 0 < ny <= n:
        x, y = nx, ny

print(x, y)

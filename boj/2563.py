# 색종이

import sys

input = sys.stdin.readline

paper = [[0 for i in range(100)] for j in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

ans = 0

for p in paper:
    ans += p.count(1)

print(ans)

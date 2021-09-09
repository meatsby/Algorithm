# 행렬 곱셈

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

ans = [[0 for _ in range(k)] for _ in range(n)]

for x in range(n):
    for y in range(m):
        for z in range(k):
            ans[x][z] += a[x][y] * b[y][z]

for i in ans:
    print(*i)

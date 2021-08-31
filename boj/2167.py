# 2차원 배열의 합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    i, j, x, y = map(lambda x: x-1, list(map(int, input().split())))
    ans = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            ans += arr[a][b]
    print(ans)

# 마인크래프트

import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
cord = [list(map(int, input().split())) for _ in range(n)]
ans = [999999999, 0]

for h in range(257):  # 평탄화 높이
    sub = 0  # 제거된 블록
    add = 0  # 필요한 블록
    for i in range(n):
        for j in range(m):
            if cord[i][j] > h:
                sub += cord[i][j] - h
            else:
                add += h - cord[i][j]
    if sub + b < add:  # 제거하고 가지고있는 블록이 필요한 블록 보다 작을 경우
        continue
    t = sub*2 + add  # 평탄화 시 걸리는 시간
    if t <= ans[0]:
        ans[0] = t
        ans[1] = h

print(*ans)

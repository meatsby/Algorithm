# 왕실의 나이트
# 파이썬 1초에 2000만번의 연산 가능

import sys
input = sys.stdin.readline

n = input().rstrip()
x = ord(n[0]) - 97
y = int(n[1]) - 1

dx = [-2, -2, -1, +1, +2, +2, +1, -1]
dy = [-1, +1, +2, +2, +1, -1, -2, -2]

ans = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        ans += 1

print(ans)

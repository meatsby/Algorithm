# 모험가 길드

import sys

input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())))

ans = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        ans += 1
        cnt = 0

print(ans)

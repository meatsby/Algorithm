# 지능형 기차 2
import sys
input = sys.stdin.readline

ans = 0
cur = 0

for _ in range(10):
    a, b = map(int, input().split())
    cur += b-a
    ans = max(ans, cur)

print(ans)

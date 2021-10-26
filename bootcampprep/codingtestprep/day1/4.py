# 덩치
import sys
input = sys.stdin.readline

spec = []
ans = []

n = int(input())

for i in range(n):
    spec.append(list(map(int, input().split())))

for _ in range(n):
    w, h = spec.pop(0)
    rank = 1
    for x, y in spec:
        if x > w and y > h:
            rank += 1
    ans.append(rank)
    spec.append((w, h))

print(*ans)
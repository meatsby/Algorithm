# 제로
import sys
input = sys.stdin.readline

ans = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        ans.pop()
    else:
        ans.append(n)

print(sum(ans))

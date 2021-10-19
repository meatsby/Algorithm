# 플러그
import sys
input = sys.stdin.readline

ans = 1
for n in range(int(input())):
    s = int(input())
    ans += s - 1

print(ans)

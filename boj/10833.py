# 사과
import sys
input = sys.stdin.readline

ans = 0

for n in range(int(input())):
    a, b = map(int, input().split())
    ans += b%a

print(ans)

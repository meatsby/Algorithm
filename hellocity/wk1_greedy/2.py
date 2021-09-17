# 백준 11047번: 동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

for c in coin:
    ans += k//c
    k %= c

print(ans)

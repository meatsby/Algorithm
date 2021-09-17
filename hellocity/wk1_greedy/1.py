# 세탁소 사장 동혁

import sys
input = sys.stdin.readline

t = int(input())
coin = [25, 10, 5, 1]

for _ in range(t):
    ans = []
    change = int(input())
    for c in coin:
        ans.append(change//c)
        change %= c
    print(*ans)

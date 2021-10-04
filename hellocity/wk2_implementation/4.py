# 백준 1110번: 더하기 사이클

import sys
input = sys.stdin.readline

n = int(input())
orig = n
ans = 0

while True:
    new = orig%10*10 + (orig//10 + orig%10)%10
    ans += 1
    if new == n:
        print(ans)
        break
    orig = new

# 곱하기 혹은 더하기

import sys

input = sys.stdin.readline

num = input().rstrip()
ans = int(num[0])

for n in num[1:]:
    if int(n) <= 1 or ans <= 1:
        ans += int(n)
    else:
        ans *= int(n)

print(ans)

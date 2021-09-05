# 완전제곱수

import sys

input = sys.stdin.readline

M = int(input())
N = int(input())
sqr = [i**2 for i in range(1, 101)]
ans = []

for s in sqr:
    if M <= s <= N:
        ans.append(s)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])

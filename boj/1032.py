# 명령 프롬프트

import sys
input = sys.stdin.readline

N = int(input())
ans = list(input().rstrip())
s = [input().rstrip() for _ in range(N-1)]

for i in range(len(ans)):
    for j in range(N-1):
        if s[j][i] != ans[i]:
            ans[i] = "?"

print("".join(ans))

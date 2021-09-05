# KMP는 왜 KMP일까?

import sys

input = sys.stdin.readline

note = list(input().split('-'))
ans = ""

for n in note:
    ans += n[0]

print(ans)

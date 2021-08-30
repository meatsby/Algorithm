# 알파벳 개수

import sys
input = sys.stdin.readline

alp = [0 for _ in range(26)]
s = input().rstrip()

for i in s:
    alp[ord(i)-97] += 1

print(*alp)

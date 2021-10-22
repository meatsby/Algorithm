# 모음의 개수
import sys
input = sys.stdin.readline

l = ["a", "e", "i", "o", "u"]
s = input().rstrip()
ans = 0

for i in s:
    if i in l:
        ans += 1

print(ans)

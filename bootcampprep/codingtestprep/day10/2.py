# 유학 금지
import sys
input = sys.stdin.readline

cam = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
s = input().rstrip()
ans = ""

for i in s:
    if i not in cam:
        ans += i

print(ans)

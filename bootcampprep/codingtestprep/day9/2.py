# 카이사르 암호
import sys
input = sys.stdin.readline

s = input().rstrip()
ans = ""

for i in s:
    ans += chr(ord(i)+23) if ord(i)-3 < 65 else chr(ord(i)-3)

print(ans)

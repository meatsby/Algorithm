# ROT13

import sys

input = sys.stdin.readline

s = input().rstrip()
ans = ""

for i in s:
    o = ord(i)
    if 65 <= o <= 90:
        o += 13
        if o > 90:
            o -= 26
    elif 97 <= o <= 122:
        o += 13
        if o > 122:
            o -= 26
    ans += chr(o)

print(ans)

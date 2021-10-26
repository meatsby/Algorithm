# 다이얼
import sys
input = sys.stdin.readline

string = input().rstrip()
ans = 0

for s in string:
    if ord(s) >= 87:
        ans += 10
    elif ord(s) >= 84:
        ans += 9
    elif ord(s) >= 80:
        ans += 8
    elif ord(s) >= 77:
        ans += 7
    elif ord(s) >= 74:
        ans += 6
    elif ord(s) >= 71:
        ans += 5
    elif ord(s) >= 68:
        ans += 4
    elif ord(s) >= 65:
        ans += 3

print(ans)
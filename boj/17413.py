# 단어 뒤집기 2

import sys

input = sys.stdin.readline

s = input().rstrip()
temp = ""
ans = ""
app = False

for i in s:
    if i == "<":
        app = True
    elif i == ">":
        ans += i
        app = False
        continue
    elif i == " ":
        if len(temp) != 0:
            ans += temp[::-1]
            temp = ""
        ans += i
        continue

    if app == True:
        if len(temp) != 0:
            ans += temp[::-1]
            temp = ""
        ans += i
    else:
        temp += i
    
print(ans + temp[::-1])

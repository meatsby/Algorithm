# 단어 뒤집기 2

import sys

input = sys.stdin.readline

# 첫 풀이
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

# 정답 참고 후 풀이
s = input().rstrip()
s = s.replace("<", "@<")
s = s.replace(">", ">@")
ss = s.split("@")
ans = ""

for i in ss:
    if len(i) != 0:
        if "<" in i:
            ans += i
        elif " " in i:
            l = [t[::-1] for t in i.split()]
            ans += " ".join(l)
        else:
            ans += i[::-1]

print(ans)

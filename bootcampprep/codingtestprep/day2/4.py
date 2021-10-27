# 그룹 단어 체커
import sys
input = sys.stdin.readline

ans = 0

for _ in range(int(input())):
    s = input().rstrip()
    isTrue = True
    for i in range(len(s)-1):
        if s[i] != s[i+1] and s[i] in s[i+1:]:
            isTrue = False
            break
    if isTrue:
        ans += 1

print(ans)

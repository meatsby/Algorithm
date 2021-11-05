# 비슷한 단어
import sys
input = sys.stdin.readline

n = int(input())
word = sorted(input().rstrip())
other = [sorted(input().rstrip()) for _ in range(n-1)]
ans = 0

wordAlp = [0] * 26

for w in word:
    wordAlp[ord(w)-65] += 1

for o in other:
    oAlp = [0] * 26
    dif = 0
    for i in o:
        oAlp[ord(i)-65] += 1

    for a in range(26):
        dif += abs(wordAlp[a] - oAlp[a])

    if abs(len(word)-len(o)) < 2 and dif < 3:
        ans += 1

print(ans)

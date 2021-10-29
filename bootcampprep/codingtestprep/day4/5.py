# 팰린드롬 만들기
import sys
input = sys.stdin.readline

alp = [0]*26
string = input().rstrip()

for s in string:
    alp[ord(s)-65] += 1

isTrue = 0
srt = ""
mid = ""

for i in range(26):
    if alp[i]%2 == 1:
        isTrue += 1
        mid += chr(i+65)
    srt += chr(i+65) * (alp[i]//2)

if isTrue >= 2:
    print("I'm Sorry Hansoo")
else:
    print(srt + mid + srt[::-1])

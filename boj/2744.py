# 대소문자 바꾸기
import sys
input = sys.stdin.readline

s = input().rstrip()

for i in s:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")

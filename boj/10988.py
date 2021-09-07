# 팰린드롬인지 확인하기

import sys

input = sys.stdin.readline

s = list(input().rstrip())

if s == list(reversed(s)):
    print(1)
else:
    print(0)

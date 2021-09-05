# 팰린드롬수

import sys

input = sys.stdin.readline

while True:
    n = list(input().rstrip())
    rn = list(reversed(n))
    if n == ['0']:
        break
    elif n == rn:
        print('yes')
    else:
        print('no')

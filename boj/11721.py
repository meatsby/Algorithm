# 열 개씩 끊어 출력하기

import sys
input = sys.stdin.readline

s = input().rstrip()
n = ""

for i in s:
    n += i
    if len(n) == 10:
        print(n)
        n = ""

if n != "":
    print(n)

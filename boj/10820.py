# 문자열 분석
import sys
input = sys.stdin.readline

while True:
    s = input()
    a, b, c, d = 0, 0, 0, 0
    for i in s:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            c += 1
        elif i == " ":
            d += 1
    if [a, b, c, d] == [0, 0, 0, 0]:
        break
    print(a, b, c, d)

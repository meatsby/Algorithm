# 문자열 재정렬
# 파이썬 1초에 2000만번의 연산 가능

import sys
input = sys.stdin.readline

n = input().rstrip()
a = []
d = 0

for i in n:
    if i.isdigit():
        d += int(i)
    else:
        a.append(i)

a.sort()

if d != 0:
    a.append(str(d))

print("".join(a))

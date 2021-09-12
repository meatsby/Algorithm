# 결혼식

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
l = [list(map(int, input().split())) for _ in range(m)]
f = []
ff = []

for x, y in l:
    if x == 1:
        f.append(y)

for x, y in l:
    if x in f:
        ff.append(y)
    elif y in f:
        ff.append(x)

fff = list(set(f + ff))
if 1 in fff:
    fff.remove(1)

print(len(fff))

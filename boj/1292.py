# 쉽게 푸는 문제

import sys

input = sys.stdin.readline

a, b = map(int, input().split())
l = []

for i in range(1, 46):
    l += [i] * i

print(sum(l[a-1:b]))

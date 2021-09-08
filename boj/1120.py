# 문자열

import sys

input = sys.stdin.readline

a, b = input().split()


def compare(a, b):
    c = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            c += 1
    return c


c = len(b) - len(a)
min_c = 51

for i in range(c+1):
    d = b[:(c-i)] + a + b[-i:]
    min_c = min(min_c, compare(d, b))

print(min_c)

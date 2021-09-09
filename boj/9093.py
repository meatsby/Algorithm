# 단어 뒤집기

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = list(input().split())
    a = [i[::-1] for i in s]
    print(" ".join(a))

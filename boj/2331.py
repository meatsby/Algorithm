# 반복수열

import sys

input = sys.stdin.readline

a, p = map(int, input().split())
d = [a]

while True:
    temp = sum([int(i)**p for i in str(d[-1])])
    if temp in d:
        print(len(d[:d.index(temp)]))
        break
    else:
        d.append(temp)

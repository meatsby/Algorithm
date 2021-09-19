# N번째 큰 수

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = sorted(list(map(int, input().split())), reverse=True)
    print(a[2])

# 홀수
import sys
input = sys.stdin.readline

a = 100
s = 0
for _ in range(7):
    n = int(input())
    if n%2 == 1:
        s += n
        a = min(a, n)

if s == 0:
    print(-1)
else:
    print(s)
    print(a)

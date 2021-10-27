# 벌집
import sys
input = sys.stdin.readline

n = int(input())

i, r1, r2 = 1, 1, 7

while True:
    if n == 1:
        print(1)
        break
    if r1 < n <= r2:
        print(i+1)
        break
    r1 = r2
    i += 1
    r2 = r1 + 6*i

# 별 찍기 - 3

import sys
input = sys.stdin.readline

N = int(input())

while True:
    if N == 0:
        break
    else:
        print('*' * N)
        N -= 1

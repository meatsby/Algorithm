# 수 정렬하기

import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])

for n in nums:
    print(n)

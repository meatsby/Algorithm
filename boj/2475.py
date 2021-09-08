# 검증수

import sys

input = sys.stdin.readline

nums = list(map(int ,input().split()))
iden = 0

for n in nums:
    iden += n ** 2

print(iden%10)

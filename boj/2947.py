# 나무 조각

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
tgt = [1, 2, 3, 4, 5]

while num != tgt:
    for i in range(4):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            print(*num)

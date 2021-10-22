# 주차의 신
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    nums = sorted(map(int, input().split()))
    print((nums[-1] - nums[0]) * 2)

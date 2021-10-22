# 대표값2
import sys
input = sys.stdin.readline

nums = sorted([int(input()) for _ in range(5)])

print(sum(nums)//5)
print(nums[2])

# 피시방 알바
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums_set = set(nums)

print(len(nums) - len(nums_set))

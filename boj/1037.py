# 약수
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))
print(nums[0] * nums[-1])

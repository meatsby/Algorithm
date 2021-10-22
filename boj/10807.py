# 개수 세기
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
print(nums.count(int(input())))

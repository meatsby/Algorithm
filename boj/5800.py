# 성적 통계
import sys
input = sys.stdin.readline

for t in range(1, int(input())+1):
    nums = list(map(int, input().split()))
    n = nums[0]
    scores = sorted(nums[1:])
    gap = 0

    for i in range(n-1):
        gap = max(scores[i+1] - scores[i], gap)

    print(f"Class {t}")
    print(f"Max {scores[-1]}, Min {scores[0]}, Largest gap {gap}")

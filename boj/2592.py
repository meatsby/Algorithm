# 대표값
import sys
from collections import Counter
input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]

print(sum(nums)//10)
print(Counter(nums).most_common(1)[0][0])

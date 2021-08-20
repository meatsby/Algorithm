# 통계학
# collections 배움

import collections

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
most = collections.Counter(nums).most_common()

print(int(round(sum(nums)/N)))
print(nums[N//2])
if len(most) > 1:
    print(most[1][0]) if most[0][1] == most[1][1] else print(most[0][0])
else:
    print(most[0][0])
print(max(nums) - min(nums))

# 에라토스테네스의 체
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [i for i in range(2, n+1)]
t = 0

while True:
    m = nums[0]
    for n in nums:
        if n%m == 0:
            ans = n
            nums.remove(n)
            t += 1
        if t == k:
            break
    if t == k:
        break

print(ans)

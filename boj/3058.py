# 짝수를 찾아라
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    nums = sorted(map(int, input().split()))
    ans = []
    for n in nums:
        if n%2 == 0:
            ans.append(n)
    print(sum(ans), ans[0])

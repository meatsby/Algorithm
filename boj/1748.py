# 수 이어 쓰기 1

import sys

input = sys.stdin.readline

nine = [0, 9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 100000001]
ans = 0
n = int(input())

for i in range(1, 10):
    if n - nine[i] < 0:
        ans += n * i
        break
    else:
        ans += nine[i] * i
        n -= nine[i]

print(ans)

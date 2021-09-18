# 시각
# 파이썬 1초에 2000만번의 연산 가능
# 완전탐색 구현 문제

import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                ans += 1

print(ans)

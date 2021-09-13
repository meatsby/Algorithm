# 숫자 정사각형

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sq = [list(input().rstrip()) for _ in range(n)]
ans = 0

for k in range(min(n, m)):
    for i in range(n-k):
        for j in range(m-k):
            if sq[i][j] == sq[i][j+k] == sq[i+k][j] == sq[i+k][j+k]:
                ans = max(ans, (k+1)**2)

print(ans)

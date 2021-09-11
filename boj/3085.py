# 사탕 게임
# 정답 참고

import sys

input = sys.stdin.readline


def inspect(c, n):
    cnt = 1
    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        for j in range(n - 1):
            # hotizontal inspection
            if c[i][j] == c[i][j + 1]:
                cnt_row += 1
            else:
                cnt = max(cnt, cnt_row)
                cnt_row = 1
            # vertical inspection
            if c[j][i] == c[j + 1][i]:
                cnt_col += 1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1

        cnt = max(cnt, cnt_row, cnt_col)
    return cnt


n = int(input())
c = [list(input().rstrip()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n - 1):
        # horizontal exchange
        if c[i][j] != c[i][j + 1]:
            c[i][j], c[i][j + 1] = c[i][j + 1], c[i][j]
            ans = max(ans, inspect(c, n))
            c[i][j], c[i][j + 1] = c[i][j + 1], c[i][j]
        # vertical exchange
        if c[j][i] != c[j + 1][i]:
            c[j][i], c[j + 1][i] = c[j + 1][i], c[j][i]
            ans = max(ans, inspect(c, n))
            c[j][i], c[j + 1][i] = c[j + 1][i], c[j][i]

print(ans)

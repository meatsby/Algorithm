# 누울 자리를 찾아라
import sys
input = sys.stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]
w, h = 0, 0
ans_w, ans_h = 0, 0

for i in range(n):
    for j in range(n):
        if board[i][j] == ".":
            w += 1
        else:
            if w > 1:
                ans_w += 1
            w = 0
        
        if board[j][i] == ".":
            h += 1
        else:
            if h > 1:
                ans_h += 1
            h = 0

    if w > 1:
        ans_w += 1
    w = 0

    if h > 1:
        ans_h += 1
    h = 0

print(ans_w, ans_h)

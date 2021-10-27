# 색종이
import sys
input = sys.stdin.readline

board = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

ans = 0

for b in board:
    ans += sum(b)

print(ans)

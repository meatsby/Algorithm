# 자리배정
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

c, r = map(int, input().split())
k = int(input())
board = [[0] * r for _ in range(c)]
x, y = 0, 0
board[x][y] = 1
i = 0

while True:
    if k > c*r:
        print(0)
        break
    if board[x][y] == k:
        print(x+1, y+1)
        break
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < c and 0 <= ny < r and board[nx][ny] == 0:
        board[nx][ny] = board[x][y] + 1
        x, y = nx, ny
    else:
        i = (i + 1) % 4

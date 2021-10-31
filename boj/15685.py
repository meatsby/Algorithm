# 드래곤 커브
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
board = [[0] * 101 for _ in range(101)]

for _ in range(int(input())):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1
    temp = [d]
    q = [d]
    for _ in range(g+1):
        for i in q:
            x += dx[i]
            y += dy[i]
            board[x][y] = 1
        q = [(t+1)%4 for t in temp]
        q.reverse()
        temp += q

ans = 0

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            ans += 1

print(ans)

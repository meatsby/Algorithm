# 치즈
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    board[nx][ny] = 0
    total = 0
    for b in board:
        total += sum(b)
    return total


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hr = 0
ans = 0
for b in board:
    ans += sum(b)

while True:
    visited = [[0]*m for _ in range(n)]
    temp = bfs(0, 0)
    hr += 1
    if temp == 0:
        print(hr)
        print(ans)
        break
    ans = temp

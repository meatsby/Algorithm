# 색종이 - 2
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    ans = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 102 and 0 <= ny < 102 and visited[nx][ny] == 0:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    ans += 1
    return ans

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [[0] * 102 for _ in range(102)]
visited = [[0] * 102 for _ in range(102)]
answer = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x+1, x+11):
        for j in range(y+1, y+11):
            board[i][j] = 1

for i in range(1, 102):
    for j in range(1, 102):
        if board[i][j] == 1 and visited[i][j] == 0:
            answer += bfs(i, j)

print(answer)

# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    visited = [[0]*n for _ in range(n)]
    visited[i][j] = 1
    edible = []
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] <= board[i][j]:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                if board[nx][ny] < board[i][j] and board[nx][ny] != 0:
                    edible.append([nx, ny, visited[nx][ny]-1])
    if not edible:
        return -1, -1, -1
    edible.sort(key=lambda x:(x[2], x[0], x[1]))
    return edible[0]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = []
n = int(input())

for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] == 9:
            board[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0

while True:
    i, j = start
    ex, ey, t = bfs(i, j)
    if ex == -1:
        break
    board[ex][ey] = board[i][j]
    board[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == board[ex][ey]:
        board[ex][ey] += 1
        exp = 0
    cnt += t

print(cnt)
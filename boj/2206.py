# 벽 부수고 이동하기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append([i, j, 1])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[i][j][1] = 1  # 시작 점 방문처리
    while q:
        x, y, penetrate = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][penetrate]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내 일 때
                if board[nx][ny] == 1 and penetrate == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1  # 방문 처리
                    q.append([nx, ny, 0])
                elif board[nx][ny] == 0 and visited[nx][ny][penetrate] == 0:
                    visited[nx][ny][penetrate] = visited[x][y][penetrate] + 1  # 방문 처리
                    q.append([nx, ny, penetrate])
    return -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs(0, 0))

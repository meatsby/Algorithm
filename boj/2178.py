# 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append([i, j])
    graph[i][j] = 0  # 시작 점 방문처리
    dist[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내일 때
                if graph[nx][ny] == 1:  # 통로일 경우
                    q.append([nx, ny])
                    graph[nx][ny] = 0  # 방문 처리
                    dist[nx][ny] = dist[x][y] + 1  # 좌표별 거리 저장
    return dist[n-1][m-1]


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]

print(bfs(0, 0))

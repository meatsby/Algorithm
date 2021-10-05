# 미로 탈출

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:  # 큐가 빌 때까지 반복
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n <= nx or nx < 0 or m <= ny or ny < 0:
                continue
            if graph[nx][ny] == 0:  # 벽인 경우 무시
                continue
            if graph[nx][ny] == 1:  # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs(0, 0))

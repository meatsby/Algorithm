# 빙산
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내일 때
                if new[nx][ny] != 0 and visited[nx][ny] == 0:  # 빙산이 이어져 있으며 방문하지 않았을 경우
                    q.append([nx, ny])
                    visited[nx][ny] = 1  # 방문 처리
    return

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
years = 1

while True:
    # 빙산이 다 녹을 때 까지 분리되지 않을 경우
    zero = 0
    for g in graph:
        zero += sum(g)
    if zero == 0:
        print(0)
        break

    # 초기화
    visited = [[0] * m for _ in range(n)]
    new = [[0] * m for _ in range(n)]
    piece = 0

    # 지구 온난화
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                temp = graph[i][j]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        temp -= 1
                if temp > 0:
                    new[i][j] = temp

    # 빙산이 몇 조각인지 확인
    for i in range(n):
        for j in range(m):
            if new[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                piece += 1

    # 빙산이 분리될 경우
    if piece > 1:
        print(years)
        break

    # 1년 후 빙산정보 업데이트
    years += 1
    graph = new

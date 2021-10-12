# 유기농 배추
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, i, j):
    q = deque()
    q.append([i, j])
    graph[i][j] = 0  # 시작 점 방문처리
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내일 때
                if graph[nx][ny] == 1:  # 집이 이어져 있을 경우
                    q.append([nx, ny])
                    graph[nx][ny] = 0  # 방문 처리
    return


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    ans = 0

    for p in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                ans += 1
    
    print(ans)

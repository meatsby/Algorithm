# 토마토
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:  # 범위 내 이면서 익지 않았을 경우
                q.append([nx, ny, nz])
                graph[nz][nx][ny] = graph[z][x][y] + 1  # 방문 처리 겸 일수 계산
    return


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for k in range(h)]
q = deque()

for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 1:
                q.append([i, j, k])  # 이미 익어있는 토마토들을 큐에 삽입

bfs()  # BFS 실행

allRipe = True
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 0:
                allRipe = False
                break
            ans = max(ans, graph[k][i][j])

if allRipe == False:
    print(-1)
elif ans == 1:
    print(0)
else:
    print(ans - 1)

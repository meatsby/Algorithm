# 단지번호붙이기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, graph, i, j):
    q = deque()
    q.append([i, j])
    graph[i][j] = 0
    houses = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 내일 때
                if graph[nx][ny] == 1:  # 집이 이어져 있을 경우
                    q.append([nx, ny])
                    graph[nx][ny] = 0  # 방문 처리
                    houses += 1
    return houses


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(n, graph, i, j))

print(len(ans))
for a in sorted(ans):
    print(a)

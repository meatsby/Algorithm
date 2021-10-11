# DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    b_visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if b_visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                b_visited[i] = 1

def dfs(v):
    d_visited[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if d_visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
d_visited = [0] * (n+1)
b_visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)

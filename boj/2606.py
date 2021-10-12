# 바이러스
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    ans = []
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        ans.append(v)
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 1
    return ans

n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

ans = bfs(1)
ans.remove(1)
print(len(ans))

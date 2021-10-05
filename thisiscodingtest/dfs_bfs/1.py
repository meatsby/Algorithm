# 음료수 얼려 먹기

import sys
input = sys.stdin.readline

def dfs(x, y):
    if n <= x or x < 0 or m <= y or y < 0:
        return False
    if graph[x][y] == 0:  # 현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 1  # 해당 노드를 방문 처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ans += 1

print(ans)

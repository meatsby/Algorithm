# 숨바꼭질
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()

        if x == k:  # 목표점에 도달했을 경우
            return visited[x] - 1

        dx = [x+1, x-1, x*2]
        for nx in dx:
            if 0 <= nx < 100001 and visited[nx] == 0:  # 범위 내 이면서 방문하지 않았을 경우
                visited[nx] = visited[x] + 1  # 방문 처리 겸 초 계산
                q.append(nx)


visited = [0] * 100001
n, k = map(int, input().split())

print(bfs(n))

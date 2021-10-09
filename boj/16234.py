# 인구 이동

from collections import deque
import sys

input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    q.append([i, j])
    union = []
    union.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:  # 한번도 간 적이 없으며 범위 내일 때
                if l <= abs(s[x][y] - s[nx][ny]) <= r:  # 두 도시의 차이가 범위 내 일 경우
                    q.append([nx, ny])
                    union.append([nx, ny])  # 연합에 소속되는 도시의 좌표
                    visited[nx][ny] = 1  # 방문 처리
    return union

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    visited = [[0]*n for _ in range(n)]
    isUnion = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1  # 방문 처리
                union = bfs(i, j)  # 방문한 도시에 대한 BFS 실행
                if len(union) > 1:  # 연합이 생성되었을 경우
                    isUnion = True  # 현재 연합이 있는 상태라고 바꿔줌
                    avg = sum([s[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        s[x][y] = avg
    if not isUnion:  # 모든 좌표를 돌았음에도 연합이 생성되지 않았다면 반복문 탈출
        break
    cnt += 1  # 모든 좌표를 돈 후 인구이동이 종료되었을 때 +1

print(cnt)

# 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append([i, j])
    board[i][j] = 1  # 시작 점 방문처리
    while q:
        x, y = q.popleft()
        if x == c and y == d:
            return board[x][y] - 1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:  # 범위 내 이면서 방문하지 않았을 경우
                board[nx][ny] = board[x][y] + 1  # 방문 처리 겸 초 계산
                q.append([nx, ny])

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for t in range(int(input())):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(bfs(a, b))

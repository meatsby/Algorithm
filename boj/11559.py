# Puyo Puyo
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    d = []
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        d.append((x, y))
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if board[nx][ny] == board[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    if len(d) >= 4:
        return d
    else:
        return []

board = [list(input().rstrip()) for _ in range(12)]
ans = 0

while True:
    # 변수 초기화
    visited = [[0]*6 for _ in range(12)]
    destroy = []

    # 중력 구현
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if board[j][i] != "." and board[k][i] == ".":
                    board[k][i] = board[j][i]
                    board[j][i] = "."
                    break

    # 터질 수 있는 그룹 전체 탐색
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                destroy += bfs(i, j)

    # 더 이상 터지지않을 때
    if len(destroy) == 0:
        break
    else:
        ans += 1

    # 터질 수 있는 모든 뿌요 터트리기
    for i, j in destroy:
        board[i][j] = "."

print(ans)

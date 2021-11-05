# 배열 돌리기 1
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
mnl = min(n, m)//2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(r):
    new = [[0]*m for _ in range(n)]
    for l in range(mnl):
        x, y = l, l
        for i in range(4):
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if l <= nx < n-l and l <= ny < m-l:
                    new[nx][ny] = board[x][y]
                    x, y = nx, ny
                else:
                    break
    board = new

for n in new:
    print(*n)

# 로봇 청소기
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int,input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def clean(r, c, d):
    global ans
    if graph[r][c] == 0:
        graph[r][c] = 2
        ans += 1

    for i in range(4):
        nd = (d+3)%4
        nx = r + dx[nd]
        ny = c + dy[nd]
        if graph[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd

    nd = (d+2)%4
    nx = r + dx[nd]
    ny = c + dy[nd]
    if graph[nx][ny] == 1:
        return
    clean(nx, ny, d)

clean(r, c, d)
print(ans)

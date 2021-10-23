# 미세먼지 안녕!
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

r, c, t = map(int, input().split())
graph = []
ux, uy = 0, 0
lx, ly = 0, 0

for i in range(r):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(c):
        if line[j] == -1:
            if ux == 0:
                ux, uy = i, j
            else:
                lx, ly = i, j

for _ in range(t):
    new = [[0] * c for _ in range(r)]  # 미세먼지 확산 후 방 상태 초기화
    dust = []  # 현재 미세먼지의 위치
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                dust.append((i, j))

    # 미세먼지 동시에 확산
    for x, y in dust:
        origin = graph[x][y]
        spread = origin//5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                new[nx][ny] += spread
                origin -= spread
        new[x][y] += origin

    # 위쪽 바람 반시계방향 순환
    udx = [-1, 0, 1, 0]
    udy = [0, 1, 0, -1]
    temp = 0
    iux = ux-1
    iuy = uy

    for i in range(4):
        while True:
            nux = iux + udx[i]
            nuy = iuy + udy[i]
            if 0 <= nux <= ux and 0 <= nuy < c:
                new[iux][iuy] = new[nux][nuy]
                iux, iuy = nux, nuy
            else:
                break
    new[ux][uy] = 0
    new[ux][uy+1] = 0

    # 아래쪽 바람 반시계방향 순환
    ldx = [1, 0, -1, 0]
    ldy = [0, 1, 0, -1]
    temp = 0
    ilx = lx+1
    ily = ly

    for i in range(4):
        while True:
            nlx = ilx + ldx[i]
            nly = ily + ldy[i]
            if lx <= nlx < r and 0 <= nly < c:
                new[ilx][ily] = new[nlx][nly]
                ilx, ily = nlx, nly
            else:
                break
    new[lx][ly] = 0
    new[lx][ly+1] = 0

    graph = new  # 방상태 업데이트

ans = 0
for g in graph:
    ans += sum(g)

print(ans)

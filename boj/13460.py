# 구슬 탈출 2
from collections import deque
import sys
input = sys.stdin.readline

def move(x, y, dx, dy):
    c = 0
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":  # 벽을 만나거나 도착점에 도착할 때 까지
        x += dx
        y += dy
        c += 1
    return x, y, c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:  # 10번 이상 기울였을 경우 실패
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != "O":  # 파란구슬이 도착점에 위치하지 않고
                if board[nrx][nry] == "O":  # 빨간구슬만 도착점에 위치했을 때
                    print(d)  # 기울인 횟수 출력 후 종료
                    return
                if nrx == nbx and nry == nby:  # 파란구슬과 빨간구슬이 겹쳤을 경우
                    if rc > bc:  # 빨간구슬이 더 많이 이동했을 경우 한 칸 뒤로
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:  # 파란구슬이 더 많이 이동했을 경우 한 칸 뒤로
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:  # 이동 후 빨간구슬과 파란구슬의 위치가 아직 한 번도 위치해보지않았던 위치라면
                    visited[nrx][nry][nbx][nby] = True  # 방문처리 이후 큐에 삽입
                    q.append([nrx, nry, nbx, nby, d+1])
    print(-1)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
board = []
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # 빨간구슬과 파란구슬의 좌표에 대한 방문좌표 선언

for i in range(n):
    line = list(input().rstrip())
    board.append(line)
    for j in range(m):
        if line[j] == "B":
            bx, by = i, j
        elif line[j] == "R":
            rx, ry = i, j

q = deque()
q.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by] = True
bfs()

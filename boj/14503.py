N, M = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for i in range(N)]
# 이동 [북, 동, 남, 서]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0


def clean(x, y, d):
    global result
    if map[x][y] == 0:
        map[x][y] = 2
        result += 1
    for i in range(4):  # 주변 스캔
        nd = (d + 3) % 4  # 회전
        nx = x + dx[nd]
        ny = y + dy[nd]
        if map[nx][ny] == 0:  # 바라보는 방향이 0 일 경우
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4  # 후진할 방향
    nx = x + dx[nd]  # x축 후진
    ny = y + dy[nd]  # y축 후진
    if map[nx][ny] == 1:  # 후진 시 벽에 닿을 때
        return
    clean(nx, ny, d)


clean(x, y, d)
print(result)

# 아기 상어

from collections import deque
import sys

input = sys.stdin.readline


def bfs(i, j):  # i, j 좌표에서 현재 아기 상어가 먹을 수 있는 모든 물고기의 위치 및 거리 찾고 가장 가까운 물고기의 정보를 반환
    visit = [[0] * n for i in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for i in range(n)]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:  # 한번도 간 적이 없으며 범위 내일 때
                if s[nx][ny] <= s[i][j] or s[nx][ny] == 0:  # 자기보다 작거나 0 일 경우 이동 가능
                    q.append([nx, ny])
                    visit[nx][ny] = 1  # 방문 처리
                    dist[nx][ny] = dist[x][y] + 1
                if s[nx][ny] < s[i][j] and s[nx][ny] != 0:  # 먹을 수 있는 물고기일 경우
                    eat.append([nx, ny, dist[nx][ny]])  # 그 물고기의 좌표 및 거리를 저장
    if not eat:  # 먹을 수 있는 물고기가 없을 경우
        return -1, -1, -1
    eat.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, 맨위, 맨왼쪽 순으로 정렬
    return eat[0][0], eat[0][1], eat[0][2]


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
s = []
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 9:  # 아기 상어 위치 확인
            s[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0

while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1: break
    s[ex][ey] = s[i][j]  # 아기 상어가 bfs 를 통해 찾은 가장 가까운 먹이를 먹고 난 후의 위치
    s[i][j] = 0
    start = [ex, ey]  # 새로운 시작 위치 설정
    exp += 1  # 한 마리 먹었다는 정보를 저장
    if exp == s[ex][ey]:  # 자신의 크기와 같은 숫자의 물고리를 먹었을 때
        s[ex][ey] += 1  # 크기가 1만큼 커짐
        exp = 0  # 초기화
    cnt += dist

print(cnt)

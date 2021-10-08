# 감시

import sys
import copy
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]], [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]  # CCTV 종류에 따른 감시 범위를 리스트로 선언

def watch(x, y, direction, temp):
    for d in direction:  # 배치에 따른 감시 방향 ex) 2번의 1번째 감시 경우의 수 [0, 1]
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = "#"
            else:
                break

def dfs(office, cctv):
    global ans
    temp = copy.deepcopy(office)  # 경우의 수에 따라 감시 범위가 달라지기 때문에 복제를 사용
    if cctv == len(cctvs):  # 총 CCTV 개수 만큼의 재귀에 들어왔을 경우 
        c = 0
        for i in temp:
            c += i.count(0)
        ans = min(ans, c)
        return

    cam_num, x, y = cctvs[cctv]

    for d in direction[cam_num]:  # CCTV 종류에 따른 감시 방향 ex) 2번 일 경우 [[0, 1], [2, 3]]
        watch(x, y, d, temp)  # [0, 1] 에 대한 감시범위 and [2, 3] 에 대한 감시범위
        dfs(temp, cctv+1)  # 다음 CCTV에 대한 DFS
        temp = copy.deepcopy(office)

n, m = map(int, input().split())
office = []
cctvs = []  # 사무실에 있는 CCTV 별 [종류, x, y]
ans = n * m
for i in range(n):
    line = list(map(int, input().split()))
    office.append(line)
    for j in range(m):
        if 0 < line[j] < 6:
            cctvs.append((line[j], i, j))

dfs(office, 0)  # CCTV 개수에 따라 경우의 수가 달라지기 때문에 DFS 사용
print(ans)

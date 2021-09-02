# 뱀
# 정답 참고

import sys

input = sys.stdin.readline
# 0 : empty
# 1 : apple
# 2 : snake

# 방향전환
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def direction(c, d):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

# 사과 배치
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input())
dirc = [0 for _ in range(10000)]

# 방향전환순간
for i in range(L):
    X, C = input().split()
    dirc[int(X)] = C

t, x, y, d = 0, 0, 0, 0
board[x][y] = 2  # initial position
snake_len = [[x, y]]  # 뱀의 길이

while True:
    t += 1

    # 다음 뱀머리가 위치 할 좌표
    x = x + dx[d]
    y = y + dy[d]

    if 0 <= x < N and 0 <= y < N and board[x][y] != 2:
        if board[x][y] == 0:  # 뱀이 사과를 먹지않는 경우
            nx, ny = snake_len.pop(0)  # 꼬리 좌표 추출
            board[nx][ny] = 0  # 꼬리 제거
        board[x][y] = 2  # 뱀 좌표 수정
        snake_len.append([x, y])  # 뱀 길이 수정
        if dirc[t] != 0:  # 방향전환순간일 경우
            d = direction(dirc[t], d)
    else:
        print(t)
        break

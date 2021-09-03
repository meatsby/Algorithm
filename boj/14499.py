# 주사위 굴리기
# 정답 참고

import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for m in move:
    if 0 <= x+dx[m-1] < N and 0 <= y+dy[m-1] < M:  # board 밖으로 나가지 않을 경우
        x += dx[m-1]
        y += dy[m-1]
        if m == 1:
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
        elif m == 2:
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
        elif m == 3:
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
        elif m == 4:
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
        
        if board[x][y] == 0:  # board가 0 일 경우 dice의 바닥면 복사
            board[x][y] = dice[2]
        else:  # board 숫자 dice 바닥면으로 복사 후 0
            dice[2] = board[x][y]
            board[x][y] = 0
        print(dice[5])

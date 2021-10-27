# 주사위 굴리기
import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

for mv in moves:
    nx = x + dx[mv]
    ny = y + dy[mv]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny

        if mv == 1:
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
        elif mv == 2:
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
        elif mv == 3:
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
        elif mv == 4:
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
        
        if board[x][y] != 0:
            dice[2] = board[x][y]
            board[x][y] = 0
        elif board[x][y] == 0:
            board[x][y] = dice[2]
        
        print(dice[5])

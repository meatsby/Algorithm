import sys
input = sys.stdin.readline

board = [[0] * 4 for _ in range(4)]
x, y = 0, 0
board[x][y] = 1

for i in range(2, 17):
    if y == 0:
        nx = x - 1
        ny = y + 1
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
        nx = x + 1
        ny = y
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
    if x == 0:
        nx = x + 1
        ny = y - 1
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
        nx = x
        ny = y + 1
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
    if y == 3:
        nx = x + 1
        ny = y - 1
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
        nx = x + 1
        ny = y
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
    if x == 3:
        nx = x - 1
        ny = y + 1
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
        nx = x
        ny = y + 1
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
            continue
    nx = x + 1
    ny = y - 1
    if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
        board[nx][ny] = i
        x, y = nx, ny
        continue
    nx = x - 1
    ny = y + 1
    if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] == 0:
        board[nx][ny] = i
        x, y = nx, ny
        continue

for b in board:
    print(b)

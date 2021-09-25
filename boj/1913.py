# 달팽이

import sys
input = sys.stdin.readline

n = int(input())
num = int(input())

snail = [[0]*n for _ in range(n)]
sx, sy = 0, 0

# when n == odd
def odd_snail(n, num):
    global sx, sy
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    snail[n//2][n//2] = 1
    d = n-1
    a, b = n**2, (n**2)-d
    x, y = 0, 0

    for s in range(n//2):
        x = s
        y = s
        for r in range(4):
            for i in range(a, b, -1):
                if i == num:
                    sx, sy = x, y
                snail[x][y] = i
                nx = x + dx[r]
                ny = y + dy[r]
                x, y = nx, ny
            a = b
            b = b - d 
        b += 2
        d -= 2

# when n == even
def even_snail(n, num):
    global sx, sy
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    snail[n//2][n//2] = 1
    d = n-1
    a, b = n**2, (n**2)-d
    x, y = 0, 0

    for s in range(n//2):
        x = s
        y = s
        for r in range(4):
            for i in range(a, b, -1):
                if i == num:
                    sx, sy = x, y
                snail[x][y] = i
                nx = x + dx[r]
                ny = y + dy[r]
                x, y = nx, ny
            a = b
            b = b - d 
        b += 2
        d -= 2

# a   b
# 49, 43, -1  6
# 43, 37, -1  6
# 37, 31, -1  6
# 31, 25, -1  6

if n%2 == 1:
    odd_snail(n, num)

for s in snail:
    print(s)
print(sx+1, sy+1)

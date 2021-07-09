import sys
import numpy as np

R, C = map(int, sys.stdin.readline().rstrip().split())
roll = np.zeros((R+2, C+2), dtype=int)
hill = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(R)]
roll[1:-1, 1:-1] = hill
result = []

if R%2 == 1:
    x, y = 1, 1
    
    while True:
        roll[x][y] = 0
        y -= 1
        if roll[x][y] != 0:
            result.append('L')
        else:
            y += 1
            x -= 1
            if roll[x][y] != 0:
                result.append('U')
            else:
                x += 1
                y += 1
                if roll[x][y] != 0:
                    result.append('R')
                else:
                    y -= 1
                    x += 1
                    result.append('D')
        if x == R and y == C:
            break
elif C%2 == 1:
    x, y = 1, 1

    while True:
        roll[x][y] = 0
        x -= 1
        if roll[x][y] != 0:
            result.append('U')
        else:
            x += 1
            y -= 1
            if roll[x][y] != 0:
                result.append('L')
            else:
                y += 1
                x += 1
                if roll[x][y] != 0:
                    result.append('D')
                else:
                    x -= 1
                    y += 1
                    result.append('R')
        if x == R and y == C:
            break
elif R%2 == 0 and C%2 == 0:
    # 제외 할 기쁨칸
    x, y = 1, 1
    min = 1001
    minx, miny = 0, 0
    
    for i in range(1, R+1):
        for j in range(1, C+1):
            if (i+j)%2 == 1 and roll[i][j] < min:
                min = roll[i][j]
                minx = i
                miny = j
    roll[minx][miny] = 0

    while True:
        roll[x][y] = 0
        y -= 1
        if roll[x][y] != 0:
            result.append('L')
        else:
            y += 1
            x -= 1
            if roll[x][y] != 0:
                result.append('U')
            else:
                x += 1
                y += 1
                if roll[x][y] != 0:
                    result.append('R')
                else:
                    y -= 1
                    x += 1
                    result.append('D')
        if x == minx and y == 1:
            break
    while True:
        roll[x][y] = 0
        x -= 1
        if roll[x][y] != 0:
            result.append('U')
        else:
            x += 1
            y -= 1
            if roll[x][y] != 0:
                result.append('L')
            else:
                y += 1
                x += 1
                if roll[x][y] != 0:
                    result.append('D')
                else:
                    x -= 1
                    y += 1
                    result.append('R')
        if x == minx+2 and y == C:
            break
    while True:
        roll[x][y] = 0
        y -= 1
        if roll[x][y] != 0:
            result.append('L')
        else:
            y += 1
            x -= 1
            if roll[x][y] != 0:
                result.append('U')
            else:
                x += 1
                y += 1
                if roll[x][y] != 0:
                    result.append('R')
                else:
                    y -= 1
                    x += 1
                    result.append('D')
        if x == R and y == C:
            break

print(roll)
print(minx, miny)
print(''.join(result))

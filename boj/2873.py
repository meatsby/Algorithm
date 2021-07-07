import sys
import numpy as np

R, C = map(int, sys.stdin.readline().rstrip().split())
roll = np.zeros((R+2, C+2), dtype=int)
hill = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(R)]
roll[1:-1, 1:-1] = hill
result = []
x, y = 1, 1

if R%2 == 1:
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

print(roll)
print(''.join(result))

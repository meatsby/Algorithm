# 톱니바퀴
import sys
input = sys.stdin.readline

def rotation(n, r):
    rotate = [0] * 5
    direct = [0] * 5
    rotate[n] = 1
    direct[n] = r

    for i in range(n, 4):
        if gears[i][2] != gears[i+1][6]:
            rotate[i+1] = 1
            direct[i+1] = -direct[i]
        else:
            break

    for i in range(n, 1, -1):
        if gears[i-1][2] != gears[i][6]:
            rotate[i-1] = 1
            direct[i-1] = -direct[i]
        else:
            break

    for i in range(1, 5):
        if rotate[i] == 1:
            if direct[i] == 1:
                gears[i].insert(0, gears[i].pop())
            else:
                gears[i].append(gears[i].pop(0))


gears = [[0]]
for _ in range(4):
    gears.append(list(map(int, list(input().rstrip()))))

for _ in range(int(input())):
    n, r = map(int, input().split())
    rotation(n, r)

ans = 0

for i in range(1, 5):
    ans += gears[i][0] * 2**(i-1)

print(ans)

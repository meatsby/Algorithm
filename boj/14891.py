# 톱니바퀴
# 정답 참고

import sys

input = sys.stdin.readline


def rotate(gn, r):
    gn -= 1
    rotation = [0 for _ in range(4)]
    direction = [0 for _ in range(4)]
    rotation[gn] = 1
    direction[gn] = r

    # 기준 톱니바퀴로부터 우측
    for i in range(gn, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotation[i + 1] = 1
            direction[i + 1] = -direction[i]
        else:
            break

    # 기준 톱니바퀴로부터 좌측
    for i in range(gn, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotation[i - 1] = 1
            direction[i - 1] = -direction[i]
        else:
            break

    # 회전방향에 따라 톱니바퀴 회전
    for i in range(4):
        if rotation[i] == 1:
            if direction[i] == 1:
                g = gears[i].pop()
                gears[i].insert(0, g)
            else:
                g = gears[i].pop(0)
                gears[i].append(g)


gears = [[int(i) for i in input().rstrip()] for _ in range(4)]
K = int(input())
for _ in range(K):
    gn, r = map(int, input().split())
    rotate(gn, r)

ans = 0

for i in range(4):
    if gears[i][0] == 1:
        ans += 2**i

print(ans)

# 경비원
import sys
input = sys.stdin.readline

def dist(i, j):
    if i == 1:
        return j
    elif i == 2:
        return w + h + w - j
    elif i == 3:
        return w + h + w + h - j
    else:
        return w + j

w, h = map(int, input().split())
distance = []

for _ in range(int(input())+1):
    i, j = map(int, input().split())
    distance.append(dist(i, j))

ans = 0

for d in distance[:-1]:
    cw = abs(distance[-1] - d)
    ccw = (w+h)*2 - cw
    ans += min(cw, ccw)

print(ans)

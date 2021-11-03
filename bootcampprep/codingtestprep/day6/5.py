# 킹
from collections import deque
import sys
input = sys.stdin.readline

d = {"R":(1, 0), "L":(-1, 0), "B":(0, -1), "T":(0, 1), "RT":(1, 1), "LT":(-1, 1), "RB":(1, -1), "LB":(-1, -1), }

king, rock, n = input().rstrip().split()
kx = ord(king[0]) - 65
ky = int(king[1]) - 1
rx = ord(rock[0]) - 65
ry = int(rock[1]) - 1

for _ in range(int(n)):
    cmd = input().rstrip()
    dx, dy = d[cmd]
    nkx = kx + dx
    nky = ky + dy
    nrx = rx + dx
    nry = ry + dy
    if 0 <= nkx < 8 and 0 <= nky < 8:
        if nkx == rx and nky == ry:
            if 0 <= nrx < 8 and 0 <= nry < 8:
                kx, ky, rx, ry = nkx, nky, nrx, nry
        else:
            kx, ky = nkx, nky

print(chr(kx+65) + str(ky+1))
print(chr(rx+65) + str(ry+1))

import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())
xl = [x1, x2, x3]
xl.sort()
yl = [y1, y2, y3]
yl.sort()
x = 0
y = 0

if xl[0] != xl[1] and xl[1] == xl[2]:
    x = xl[0]
else:
    x = xl[2]

if yl[0] != yl[1] and yl[1] == yl[2]:
    y = yl[0]
else:
    y = yl[2]

print(x, y)

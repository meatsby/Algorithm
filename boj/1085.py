import sys

x, y, w, h = map(int, sys.stdin.readline().split())
x_min = w - x
y_min = h - y
rect = [x, y, x_min, y_min]

print(min(rect))

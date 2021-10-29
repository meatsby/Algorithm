# 공
import sys
input = sys.stdin.readline

cups = [1, 2, 3]

for _ in range(int(input())):
    x, y = map(int, input().split())
    idx_x = cups.index(x)
    idx_y = cups.index(y)
    cups[idx_x] = y
    cups[idx_y] = x

print(cups[0])

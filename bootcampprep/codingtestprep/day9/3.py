# 성 지키기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
re_b = list(map(list, zip(*board)))
r, c = 0, 0

for b in board:
    if "X" in b:
        r += 1

for re in re_b:
    if "X" in re:
        c += 1

print(max(n-r, m-c))

# 상근날드
import sys
input = sys.stdin.readline

burgers = sorted([int(input()) for _ in range(3)])
drinks = sorted([int(input()) for _ in range(2)])

print(burgers[0] + drinks[0] - 50)

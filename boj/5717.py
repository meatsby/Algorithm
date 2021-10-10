# 상근이의 친구들
import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0:
        break
    print(a + b)

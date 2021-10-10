# 과자
import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())
need = k*n - m
if need < 0:
    print(0)
else:
    print(need)

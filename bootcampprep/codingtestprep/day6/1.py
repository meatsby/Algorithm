# 상금 헌터
import sys
input = sys.stdin.readline

A = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
B = [0, 512, 256, 256, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a >= len(A):
        a = 0
    if b >= len(B):
        b = 0
    print((A[a] + B[b]) * 10000)
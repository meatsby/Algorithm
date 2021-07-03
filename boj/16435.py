import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
h = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    if h[i] <= L:
        L += 1

print(L)

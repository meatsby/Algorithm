import sys

N = int(sys.stdin.readline().rstrip())
l = sorted([int(sys.stdin.readline().rstrip()) for i in range(N)], reverse=True)

for i in range(N):
    l[i] *= i+1

print(max(l))

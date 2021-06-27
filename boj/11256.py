import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    J, N = map(int, sys.stdin.readline().rstrip().split())
    l = []
    for j in range(N):
        R, C = map(int, sys.stdin.readline().rstrip().split())
        l.append(R*C)
    l.sort(reverse=True)
    result = 0
    for k in l:
        J -= k
        result += 1
        if J <= 0:
            print(result)
            break

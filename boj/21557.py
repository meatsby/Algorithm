import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
L = [A[0]-1, A[N-1]-1]

for i in range(N-3):
    if L[0] >= L[1]:
        L[0] -= 1
    else:
        L[1] -= 1

print(max(L))

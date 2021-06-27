import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N, M = map(str, sys.stdin.readline().rstrip().split())
    cnt = abs(N.count('1')-M.count('1'))
    dif = 0
    for i in range(len(N)):
        if N[i] != M[i]:
            dif += 1
    print((dif-cnt)//2 + cnt)

import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    l = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)])

    cnt = 1
    max = l[0][1]

    for i in range(1,N):
        if max > l[i][1]:
            cnt += 1
            max = l[i][1]
    
    print(cnt)

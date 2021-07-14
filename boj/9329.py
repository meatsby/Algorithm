T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    stype = list(map(int, input().split()))
    prz = 0
    for i in range(N):
        rwd = 1000001
        for j in l[i][1:l[i][0]+1]:
            if stype[j-1] < rwd:
                rwd = stype[j-1]
        prz += rwd*l[i][-1]
    print(prz)

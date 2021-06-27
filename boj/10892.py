import sys

N = int(sys.stdin.readline().rstrip())
tri = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(3*N)]
s_tri = sorted(tri, key=lambda t: (t[1], -t[0]))
l = []

for i in s_tri:
    l.append(tri.index(i)+1)
    if len(l) == 3:
        print(*sorted(l))
        l = []

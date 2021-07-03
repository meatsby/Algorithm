import sys

N = int(sys.stdin.readline().rstrip())
t = [1, 100000]

for i in range(N):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    if s > t[0]:
        t[0] = s
    if e < t[1]:
        t[1] = e

if t[0] - t[1] < 0:
    print(0)
else:
    print(t[0] - t[1])

import sys
day = 1
N = int(sys.stdin.readline().rstrip())
t = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)

for i in range(N):
    t[i] += day + 1
    day += 1

print(max(t))

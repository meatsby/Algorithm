import sys

N = int(sys.stdin.readline().rstrip())
l = []
result = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    l.append([a, b])

l.sort()

for i in range(N):
    if l[i][0] > result:
        result = l[i][0]
    result += l[i][1]

print(result)

import sys

N = int(sys.stdin.readline().rstrip())
j = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
s = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
score = 0
k = 0

for i in range(N):
    if j[i] < s[k]:
        score += 1
        k += 1

if score >= (N+1)/2:
    print('YES')
else:
    print('NO')

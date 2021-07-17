# 런타임 에러로 인해 다시 시도

import sys

N = int(sys.stdin.readline().rstrip())
P = list(int(sys.stdin.readline().rstrip()) for i in range(N))
result = []
bomb = 1

for i in range(1, N):
    if P[i-1] < P[i]:
        bomb = i+1
    elif P[i-1] > P[i]:
        result.append(bomb)
    elif P[i-1] == P[i]:
        result.append(bomb)
        bomb = i+1
result.append(bomb)

for i in set(result):
    print(i)

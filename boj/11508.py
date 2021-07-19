# 2+1 세일

N = int(input())
C = sorted([int(input()) for i in range(N)], reverse=True)
P = 0

for i in range(N):
    if i%3 != 2:
        P += C[i]

print(P)

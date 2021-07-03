import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
l = [i for i in range(1, K+1)]

if N < sum(l):
    print(-1)
elif (N-sum(l))%K == 0:
    print(K-1)
else:
    print(K)

# 1 2 3 = 6 / 2
# 1 2 4 = 7 / 3
# 1 3 4 = 8 / 3
# 2 3 4 = 9 / 2
# 2 3 5 = 10 / 3
# 2 4 5 = 11 / 3
# 3 4 5 = 12 / 2

# 1 2 3 4 = 10 / 3
# 1 2 3 5 = 11 / 4
# 1 2 4 5 = 12 / 4
# 1 3 4 5 = 13 / 4
# 2 3 4 5 = 14 / 3
# 2 3 4 6 = 15 / 4
# 2 3 5 6 = 16 / 4
# 2 4 5 6 = 17 / 4
# 3 4 5 6 = 18 / 4

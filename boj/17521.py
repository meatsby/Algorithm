import sys

n, W = map(int, sys.stdin.readline().rstrip().split())
s = [int(sys.stdin.readline().rstrip()) for i in range(n)]
coin = 0

for i in range(1, n):
    if s[i] > s[i-1]:
        coin += W//s[i-1]
        W %= s[i-1]
    elif s[i] < s[i-1]:
        W += coin*s[i-1]
        coin = 0


print(W + coin*s[n-1])

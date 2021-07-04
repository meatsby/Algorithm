import sys

X, Y = map(int, sys.stdin.readline().rstrip().split())

print(X + Y + min(X, Y)//10)

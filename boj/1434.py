import sys

n, m = map(int, sys.stdin.readline().split())
box = list(map(int, sys.stdin.readline().split()))
book = list(map(int, sys.stdin.readline().split()))

print(sum(box)-sum(book))

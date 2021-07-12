import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
book = list(map(int, sys.stdin.readline().rstrip().split()))
book.reverse()
sum = 0
box = 0

for i in book:
    if i > M:
        continue
    sum += i
    if sum > M:
        box += 1
        sum = i
    elif sum == M:
        box += 1
        sum = 0
if sum != 0:
    box += 1

print(box)

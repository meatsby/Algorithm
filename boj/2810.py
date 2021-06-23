import sys

n = int(sys.stdin.readline().rstrip())
seats = sys.stdin.readline().rstrip()
count = seats.count('LL')

if count < 1:
    print(n)
else:
    print(n - count + 1)

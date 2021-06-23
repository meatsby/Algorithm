import sys

n = int(sys.stdin.readline().rstrip())
rem = 1000 - n
type = [500, 100, 50, 10, 5, 1]
count = 0

for coin in type:
    count += rem//coin
    rem %= coin

print(count)

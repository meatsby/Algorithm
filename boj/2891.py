import sys

n, s, r = map(int, sys.stdin.readline().rstrip().split())
damaged = list(map(int, sys.stdin.readline().rstrip().split()))
onemore = list(map(int, sys.stdin.readline().rstrip().split()))
count = s

for i in range(s):
    for j in range(r):
        if damaged[i]==onemore[j] or abs(damaged[i]-onemore[j])==1:
            count -= 1
            del onemore[j]
            r -= 1
            break

print(count)

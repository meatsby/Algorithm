import sys

n = int(sys.stdin.readline().rstrip())
gg = [1, 2]

if n%2 == 0:
    gg *= n//2
else:
    gg *= n//2
    gg.append(3)

print(*gg)

import sys

while True:
    t = sorted(list(map(int, sys.stdin.readline().split())))
    if sum(t) == 0:
        break
    if t[0]**2 + t[1]**2 == t[2]**2:
        print('right')
    else:
        print('wrong')

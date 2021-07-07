import sys

bcd = list(map(int, sys.stdin.readline().rstrip().split()))
burger = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
side = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
beverage = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
total = sum(burger)+sum(side)+sum(beverage)
set_d = 0

for i in range(min(bcd)):
    set_d += burger[i] + side[i] + beverage[i]

print(total)
print(int(total - set_d + set_d * 0.9))

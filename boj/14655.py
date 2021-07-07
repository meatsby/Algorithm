import sys

n = int(sys.stdin.readline().rstrip())
first = list(map(int, sys.stdin.readline().rstrip().split()))
second = list(map(int, sys.stdin.readline().rstrip().split()))
f_sum = 0
s_sum = 0

for i in first:
    if i < 0:
        f_sum += -i
    else:
        f_sum += i

for i in second:
    if i > 0:
        s_sum += -i
    else:
        s_sum += i

print(f_sum - s_sum)

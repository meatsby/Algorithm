import sys

N = int(sys.stdin.readline().rstrip())
neg = []
num = []
pos = []

for i in range(N):
    s = int(sys.stdin.readline().rstrip())
    if s < 0:
        neg.append(s)
    elif s > 1:
        pos.append(s)
    else:
        num.append(s)

sum = sum(num)
neg.sort(reverse=True)
pos.sort()

if len(neg)%2 == 0:
    for i in range(1, len(neg), 2):
        sum += neg[i-1]*neg[i]
else:
    for i in range(2, len(neg), 2):
        sum += neg[i-1]*neg[i]
    if 0 not in num:
        sum += neg[0]

if len(pos)%2 == 0:
    for i in range(1, len(pos), 2):
        sum += pos[i-1]*pos[i]
else:
    sum += pos[0]
    for i in range(2, len(pos), 2):
        sum += pos[i-1]*pos[i]

print(sum)

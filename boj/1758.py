N = int(input())
tip = sorted([int(input()) for i in range(N)], reverse=True)
sum = 0

for i in range(N):
    tip[i] -= i

for i in tip:
    if i > 0:
        sum += i

print(sum)
